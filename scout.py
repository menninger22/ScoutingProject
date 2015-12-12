# Contains the main loop for the scouting program.

import urllib2
import sys
import os

from Tkinter import *
from drawing import *
from player import *

# Takes a string (a word from the play-by-play), and determines which position
# the ball was hit to. 
def getPosition(pos):
    if 'rf' in pos:
        return 9
    elif 'cf' in pos:
        return 8
    elif 'lf' in pos:
        return 7
    elif 'ss' in pos:
        return 6
    elif '3b' in pos:
        return 5
    elif '2b' in pos:
        return 4
    elif '1b' in pos:
        return 3
    elif 'c' in pos:
        return 2
    elif 'p' in pos:
        return 1
    return 0


# Note: At the moment, I'm ignoring errors, fielder's choices, and sacrifices. Not as easy to parse.

# Parses the play-by-play of a game. Looks for hits, outs, walks, HBPs.
def parseGame(plays, team):

    for line in plays.readlines():
        # Remove the newline character at the end of the line
        line = line.rstrip()

        # Seems that RBI hits have this extra tag up front in the HTML code. Remove if it's there.
        line = line.replace('<strong>', '', 1)

        if line != '' and line[0].isupper():
            words = line.split(' ')

            # Get the name of the batter
            first = words[0]
            last = words[1]

            foundPlayer = None

            # Search for the player within the team. Stop when found.
            players = team.get_players()
            for player in players:
                # First Last
                if first == player.get_info()[0] and last == player.get_info()[1]:
                    #print (first, last), " Play: ", line
                    foundPlayer = player
                    break
                # Last
                elif first == player.get_info()[1] and last[0].islower():
                    #print (first), " ONLY LAST: ", line
                    # Add a placeholder as to not mess up the parsing
                    words.insert(0, "Placeholder")
                    foundPlayer = player
                    break
                # Last, Fi. 
                # Note: remove the last char of 'last', since it might be punctuation eg '.'
                elif first == player.get_info()[1] and last[:-1] in player.get_info()[0]:
                    #print "LAST, FI: ", line
                    foundPlayer = player
                    break
                # Some also are First La. 
                # Note: remove the last char of 'last', since it might be punctuation eg '.'
                elif first == player.get_info()[0] and last[:-1] in player.get_info()[1]:
                    #print 'FIRST, LA: ', line
                    foundPlayer = player
                    break 

            # If we couldn't find the player, just ignore.
            if foundPlayer == None:
                continue
            
            # Determine what happened on the play.
            if 'walk' in line:
                foundPlayer.add_walk()
            elif 'hit by pitch' in line:
                foundPlayer.add_hbp()
            elif 'struck out' in line:
                foundPlayer.add_so()
            elif 'flied out' in line or 'poppped out' in line or 'popped up' in line or 'fouled out' in line:
                # Ex. First Last flied out to rf
                location = getPosition(words[5])
                foundPlayer.add_out('f', location)
            elif 'grounded out' in line:
                # Ex. First Last grounded out to ss
                location = getPosition(words[5])
                foundPlayer.add_out('g', location)
            elif 'grounded into double play' in line:
                # Don't forget to look for double plays
                # Ex. First Last grounded into double play 2b to ss to 1b
                location = getPosition(words[6])
                foundPlayer.add_out('g', location)
            elif 'out at first' in line:
                # Awkward wording for groundouts to first
                # Ex. First Last out at first 1b unassisted.
                location = getPosition(words[5])
                foundPlayer.add_out('g', location)
            elif 'lined out' in line:
                # Ex. First Last lined out to rf
                location = getPosition(words[5])
                foundPlayer.add_out('l', location)
            elif 'singled' in line or 'doubled' in line or 'tripled' in line or 'homered' in line:
                # Ex. First Last doubled to left center

                # First, determine how many bases.
                slug = 0
                if 'singled' in line:
                    slug = 1
                elif 'doubled' in line:
                    slug = 2
                elif 'tripled' in line:
                    slug = 3
                elif 'homered' in line:
                    slug = 4


                # Determine if the play was a bunt or not.
                bunt = False
                if 'bunt' in line:
                    bunt = True

                # Determine where the hit was. Note that hits to the outfield 
                # can have multiple wordings.
                if 'to left' in line or 'through the left side' in line or 'to deep left' in line or 'down the left field line' in line: 
                    location = 7
                elif 'to center' in line or 'up the middle' in line or 'to deep center' in line:
                    location = 8
                elif 'to right' in line or 'through the right side' in line or 'to deep right' in line or 'down the right field line' in line:
                    location = 9
                elif 'to pitcher' in line:
                    location  = 1
                elif 'singled to third' in line:
                    location = 5
                elif 'singled to short' in line:
                    location  = 6
                elif 'singled to second' in line:
                    location = 4
                elif 'singled to first' in line:
                    location = 3
                elif 'singled to catcher' in line:
                    location = 2
                else:
                    # print 'Could not determine location: ', line
                    # Couldn't determine where hit was. Just call it to pitcher for now.
                    location = 1

                # Finally, record the hit for the player
                foundPlayer.add_hit(bunt, location, slug) 
      

# Draws and saves the spray chart for each player on the team.
def scoutPlayers(team, teamName):

    # make the team directory if necessary
    if not os.path.isdir(teamName):
        os.makedirs(teamName)

    players = team.get_players()
    for player in players:
        stats = player.get_stats() # (outs, hits, AB's, walks, hbp, K's)
        if stats[2] == 0:
            # if no AB's, just skip
            continue
        spray = player.get_spray()
        drawField(player, spray, teamName)


# Enter the main loop for the program.
if __name__ == "__main__":

    # To be determined: how to enter the play-by-play data. Text files, URLs?

    # For now, lets just read in some arguments corresponding to text files
    if len(sys.argv) < 4:
        print "USAGE: python scout.py <Team Name> <Team Roster> <Team Games>"
    teamName = None
    rosterFile = None
    gamesFile = None
    if len(sys.argv) >= 3:
        # We will save the images in the teamName directory.
        teamName = str(sys.argv[1])
        rosterFile = str(sys.argv[2])
        gamesFile = str(sys.argv[3])


    # Create the team
    team = Team(teamName)

    # Go through the roster, and add each player to the team
    roster = open(rosterFile, 'r')
    for line in roster:
        # Remove the newline character at the end of the line
        line = line.rstrip()
        name = line.split(" ")
        first = name[0]
        last = name[1]
        team.add_player(Player(first, last, 'R', 'R', [1], 2015, 1))

    # Go through the play-by-play URLs, and parse each game
    games = open(gamesFile, 'r')
    for url in games:
        # Remove the newline character at the end of the line
        url = url.rstrip()
        if url == "" or url[0] == '#':
            continue
        plays = urllib2.urlopen(url)
        parseGame(plays, team)

    # When we finish parsing the games, this will draw and save the spray 
    # charts for each player.
    scoutPlayers(team, teamName)

