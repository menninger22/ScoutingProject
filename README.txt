Created: March, 2015


Usage: python scout.py [teamName] [rosterFile] [gamesFile]

The teamName will be the name of the directory created that will contain
the scouting report.

rosterFile will contain the names of all of the players.  This assumes that every name is two names, First Last, separated by a space.

gamesFile is a list of URLs of play-by-plays for this team with these players.

This will create a .ps file for each player with a “scouting report” for
them, color coded by tendency.  The higher the proportion of hits to a
particular part of the field, the darker the red for that region will be.




Note: This was done in about a week.  I expect to work on it again this
winter.  The first thing I would like to change is the output.  Ideally,
this would output all files into one file.  Then, I want to make the user
input as little as possible.  I would like to make it so the user does
not need to enter the file himself, and then I would like to explore the
possibility of self-navigating to the play-by-plays given the URL of the
results page.