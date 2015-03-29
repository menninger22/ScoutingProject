
import urllib2

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


# At the moment, i'm ignoring errors and fielders choices. too hard to parse.
# Still would also like to add SH and SF
# Parses the play-by-play of a game. Looks for hits, outs, walks, HBPs.
def parseGame(plays):

    for line in plays.readlines():
        # remove the newline character at the end
        line = line.rstrip()

        # Seems that RBI hits have this extra tag up front. Remove if it's there.
        line = line.replace('<strong>', '', 1)

        if line != '' and line[0].isupper():
            #print "Play: ", line
            words = line.split(' ')

            # get the name of the batter
            first = words[0]
            last = words[1]

            #print line
            #print words

            if 'walk' in line:
                #print line
                print 'Walk!'
                #add_walk()
            elif 'hit by pitch' in line:
                #print line
                print 'HBP'
                #add_hbp()
            elif 'struck out' in line:
                #print line
                print 'SO'
                # add_so()
            elif 'flied out' in line or 'poppped out' in line:
                #print line
                #print words
                location = getPosition(words[5])
                #print 'FO: ', location
                # add_out('f', location)
            elif 'grounded out' in line:
                #print line
                #print words
                location = getPosition(words[5])
                #print 'GO: ', location
                # add_out('g', location)
            elif 'lined out' in line:
                location = getPosition(words[5])
                # add_out('l', location)

            elif 'singled' in line or 'doubled' in line or 'tripled' in line or 'homered' in line:

                #print line
                slug = 0
                if 'singled' in line:
                    slug = 1
                elif 'doubled' in line:
                    slug = 2
                elif 'tripled' in line:
                    slug = 3
                elif 'homered' in line:
                    slug = 4

                # for hits, first look for 'left', 'center', 'right'
                # if not, look for position in words[5]
                # finally, look for 'bunt'

                # Check if this was a bunt hit
                bunt = False
                if 'bunt' in line:
                    bunt = True

                # will also get to 'left center', etc
                if 'to left' in line or 'through the left side' in line:
                    location = 7
                    #add_hit(bunt, 7, 1)
                elif 'to center' in line or 'up the middle' in line:
                    location = 8
                    #add_hit(bunt, 8, 1)
                elif 'to right' in line or 'through the right side' in line:
                    location = 9
                    #add_hit(bunt, 9, 1) 
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
                    print 'Couldnt parse hit: ', line
                    #location = getPosition(words[5])

                #print line
                #print 'HIT bases = ', slug, ' location = ' , location, ' bunt? ', bunt
                #add_hit(bunt, location, slug)
            #else:
                # NOTE: not parsing errors and fielder's choices at the momement
                #print 'COULD NOT PARSE: ', line
        

# Enter the main loop for the program. Still TBD how to enter the play-by-play
# data to be parsed
if __name__ == "__main__":

    # Still need to load rosters somehow

    url = 'http://www.gocaltech.com/sports/bsb/2014-15/boxscores/20150227_7wrf.xml?view=plays'
    plays = urllib2.urlopen(url)

    parseGame(plays)




"""
def parse_roster(url):
    roster = urllib2.urlopen(url)
    for line in roster.readlines():
        print line
        #if 'Fr' in line or 'So' in line or 'Jr' in line or 'Sr' in line:
            #print "Name: ", line
            #if 'single' in line:
            #    record_hit()

parse_roster('http://www.clusports.com/baseball/roster/')
"""