from Tkinter import * 
from player import *

# Given a list of percentages to each of the 9 positions, determines the 
# color to use in the spray chart. If a player hits to a position less
# than 10% of the time, it will remain white. Otherwise, we color the section
# red and make the color brighter as the percentage gets higher.
def setColors(percents):
    colors = []
    for i in percents:
        # Make the red darker if i is greater, which indicates more hits...
        redness = max(255 - (5 * i), 0)
        color = '#%02x%02x%02x' % (255, redness, redness)
        colors.append(color)
    return colors

# Given a list of percentages to each of the 9 positions, determines the text
# that should be overlaid on the section. For example, if a player hits 1/3 
# of balls to LF, that section will say '33%'. Note that we just round to
# an integer.
def setText(percents):
    percentages = []
    for i in percents:
        percentage = str(i) + '%'
        percentages.append(percentage)
    return percentages


# Draws the spray chart for a Player, and saves the image as a PostScript
# file, with the filename as FirstLast.ps.
def drawField(player, spray, teamName):

    root = Tk() 
    canvas = Canvas(bg='white', width = 800, height = 600) 
    canvas.pack() 

    center_x = 400
    center_y = 500
    
    # Get the sum of the elements in spray to normalize it (some locations
    #   did not get recorded as they were invalid)
    total_obs = sum(spray)
    
    # Turn the normalized spray array into actual percentages.
    if total_obs != 0:
        percents = [int(i / total_obs * 100) for i in spray] 
    else:
        percents = [0 for i in spray]

    # Determine final colors and text
    colors = setColors(percents)
    texts = setText(percents)

    # Draw the outfield arc.
    outfield_distance = 300
    outfield = [center_x - outfield_distance, center_y - outfield_distance, center_x + outfield_distance, center_y + outfield_distance]
    canvas.create_arc(outfield, start=110, extent = 40, fill=colors[6]) # LF
    canvas.create_arc(outfield, start=70, extent = 40, fill=colors[7]) # CF
    canvas.create_arc(outfield, start=30, extent = 40, fill=colors[8]) # RF

    # Draw infield arc.
    infield_distance = 175
    infield = [center_x - infield_distance, center_y - infield_distance, center_x + infield_distance, center_y + infield_distance]
    canvas.create_arc(infield, start=120, extent = 30, fill=colors[4]) # 3B
    canvas.create_arc(infield, start=90, extent = 30, fill=colors[5]) # SS
    canvas.create_arc(infield, start=60, extent = 30, fill=colors[3]) # 2B
    canvas.create_arc(infield, start=30, extent = 30, fill=colors[2]) # 1B

    # Outfield stats: LF, CF, RF
    canvas.create_text(235, 335, text=texts[6], fill="black", font="Helvetica 18 bold underline") # LF
    canvas.create_text(400, 275, text=texts[7], fill="black", font="Helvetica 18 bold underline") # CF
    canvas.create_text(575, 335, text=texts[8], fill="black", font="Helvetica 18 bold underline") # RF

    # Infield stats: 3B, SS, 2B, 1B
    canvas.create_text(310, 410, text=texts[4], fill="black", font="Helvetica 18 bold underline") # 3B
    canvas.create_text(370, 380, text=texts[5], fill="black", font="Helvetica 18 bold underline") # SS
    canvas.create_text(430, 380, text=texts[3], fill="black", font="Helvetica 18 bold underline") # 2B
    canvas.create_text(490, 410, text=texts[2], fill="black", font="Helvetica 18 bold underline") # 1B

    info = player.get_info()
    stats = player.get_stats() # (outs, hits, ab, walks, HBP, SO)

    # compute batting average
    BA = .000
    if stats[2] != 0:
        BA = float(len(stats[1])) / float(stats[2])
    avg = "{0:.3f}".format(BA)
    avg = avg[1:] # chop off the leading 0 in the average
    stats_text = "  BA: " + str(avg) + "   "+ str(stats[5]) + "K   " + str(stats[3]) + "BB   " + str(stats[4]) + "HBP"
    name_info = info[0] + ' ' + info[1]

    canvas.create_text(385, 69, text=name_info, fill="black", font="Helvetica 26 bold")
    canvas.create_text(375, 120, text=stats_text, fill="black", font="Helvetica 20")

    # Update the image and save the file.
    canvas.update() 
    info = player.get_info()
    name = info[0] + "_" + info[1]
    fileName = teamName + '/' + name + '.ps'
    canvas.postscript(file = fileName) 

    # Uncomment to have popups stay.
    root.mainloop()
    root.quit()

