# Hit:
# 	Description:
#		This class takes care of hits, storing whether it was a bunt, where the hit
#		was to and how many bases were reached on the hit.
#
#	Attributes:
#		is_bunt:  Boolean denoting bunt hit or not
#		location: Integer 1-9 for player/area in field hit to
#		slug:     Integer 1-4 for total bases
#
class Hit:
	def __init__(self, is_bunt, loc, slug):
		self.is_bunt  = is_bunt		# Boolean denoting bunt hit or not
		self.location = loc			# Integer 1-9 for player hit to
		self.slug     = slug		# Integer 1-4 for 1B, 2B, 3B, HR

# Out:
# 	Description:
#		This class takes care of outs, storing what kind of out was recorded (line out,
#		fly out or ground out) as well as where the out was recorded.
#
#	Attributes:
#		type:	  Records the type of out: l - lineout, f - flyout, g - groundout,
#				  e - error, s - sacrifice
#		location: Integer 1-9 for player/area in field hit to
#	
class Out:
	def __init__(self, type, loc):
		self.type     = type
		self.location = loc

# Player:
#	Description:
#		This class contains information about the hitter including basic information
#		such as name, number, position as well as personal statistics.
#
#	Attributes:
#		first: String for player first name
#		last:  String for player last name
#		bat:   Character for left/right/switch hitter
#		throw: Character for lefty/righty thrower
#		pos:   List of Integers for positions played
#		year:  Integer for graduation year
#		num:   Integer for player jersey number
#
#		outs:  List of Outs (Out class defined above)
#		hits:  List of Hits (Hit class defined above)
#		ab:	   Integer for number of at-bats
#		walks: Integer for number of walks
#		hbp:   Integer for number of hit by pitches
#		so:    Integer for number of strike outs
#
#	Functions:
#		init:	     Initializes attributes
#		get_info:    Returns basic information about hitter
#		get_stats:   Returns hitter statistics
#		edit_player: Edits the basic info about the player
#		add_hit:     Takes hit info and updates attributes after adding given hit
#		add_so:	     Updates attributes to reflect one more strike out
#		add_hbp:     Updates attributes to reflect one more hit batter
#		add_walk:    Updates attributes to reflect one more walk
#		add_out:     Takes out info and updates attributes after adding given out
#		get_avg:     Returns player batting average
#		get_obp:     Returns player on base percentage
#		get_slg:     Returns player slugging percentage
#		get_spray:   Returns proportions of hits to each part of the field
#
class Player:
	# init:
	#	Description:
	#		Initializes player.
	#
	#	Arguments:
	#		fn (String)    		- first name
	#		ln (String)    		- last name
	#		b  (Character) 	 	- batting side ('R', 'L' or 'S')
	#		th (Character) 		- throwing arm ('R' or 'L')
	#		po (Integer List)   - list of positions (1 - 9)
	#		yr (Integer)		- graduation year
	#		no (Integer)		- jersey number
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.first
	#		self.last
	#		self.bat
	#		self.throw
	#		self.pos
	#		self.year
	#		self.num
	#		self.outs
	#		self.hits
	#		self.ab
	#		self.walks
	#		self.hbp
	#		self.so
	#
	def __init__(self, fn, ln, b, th, po, yr, no):
		self.first = fn
		self.last  = ln
		self.bat   = b
		self.throw = th
		self.pos   = po
		self.year  = yr
		self.num   = no
		
		self.outs  = []
		self.hits  = []
		self.ab    = 0
		self.walks = 0
		self.hbp   = 0
		self.so    = 0
		
	# get_info:
	#	Description:
	#		Returns all of the personal information about the player.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		first name (String)
	#		last name (String)
	#		batting side ('L' 'R' or 'S')
	#		throwing arm ('L' or 'R')
	#		position(s) (List of Integers)
	#		year (Integer)
	#		number (Integer)
	#
	def get_info(self):
		return (self.first, self.last, self.bat, self.throw,
				self.pos, self.year, self.num)
				
	# get_stats:
	#	Description:
	#		Returns player's statistics.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		self.outs (List of Outs)
	#		self.hits (List of Hits)
	#		self.ab (Integer)
	#		self.walks (Integer)
	#		self.hbp (Integer)
	#		self.so (Integer)
	#
	def get_stats(self):
		return (self.outs, self.hits, self.ab, self.walks, self.hbp, self.so)
		
	# edit_player:
	#	Description:
	#		Changes personal information of the player.  Replacing any argument with None
	#		will leave the attribute as it was.
	#
	#	Arguments:
	#		bat ('R' 'L' or 'S')
	#		throw ('R' or 'L')
	#		pos (List of Integers) - 1-9 for the positions on the field
	#		year (Integer) - graduation year
	#		num (Integer) - jersey number
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.bat
	#		self.throw
	#		self.pos
	#		self.year
	#		self.num
	#
	def edit_player(self, bat, throw, pos, year, num):
		if bat != None:
			self.bat = bat
		if throw != None:
			self.throw = throw
		if pos != None:
			self.pos = pos
		if year != None:
			self.year = year
		if num != None:
			self.num = num
		return
		
	# add_hit:
	#	Description:
	#		Adds a hit to the player's list of hits.
	#
	#	Arguments:
	#		is_bunt (Boolean) - true if the hit was from a bunt, false otherwise
	#		loc (Integer)     - (1 - 9) denoting where in the field the hit was to
	#		slg (Integer)     - (1 - 4) denoting total bases on the hit
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.hits - adds hit to list
	#		self.ab   - adds 1 to at-bat total
	#
	def add_hit(self, is_bunt, loc, slg):
		new_hit = Hit(is_bunt, loc, slg)	# Hit to be recorded
		self.hits.append(new_hit)
		self.ab += 1
		return
		
	# add_so:
	#	Description:
	#		Adds a strikeout to player's stats.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.so - adds 1 to strike out count
	#		self.ab - adds 1 to at-bat count
	#
	def add_so(self):
		self.so += 1
		self.ab += 1
		return
	
	# add_hbp:
	#	Description:
	#		Adds to hit by pitch count and updates related stats.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.hbp - adds 1 to hit-by-pitch count
	#
	def add_hbp(self):
		self.hbp += 1
		return
		
	# add_walk:
	#	Description:
	#		Adds one to the walk count.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.walks - adds 1 to walks count
	#
	def add_walk(self):
		self.walks += 1
		return
	
	# add_out:
	#	Description:
	#		Adds an out to the list of outs and changes the relevant statistics.
	#
	#	Arguments:
	#		type (Character) - records how the out happened. g - ground out,
	#						   f - fly out, l - line out, e - error, s - sacrifice
	#		loc (Integer)    - records where the out went, 1 - 9 for positions in the
	#						   field
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		self.outs - adds to list of out using given information
	#		self.ab   - incremented if not a sacrifice
	#
	def add_out(self, type, loc):
		new_out = Out(type, loc)
		self.outs.append(new_out)
		if type != 's':
			self.ab += 1
		return
		
	# get_avg:
	#	Description:
	#		Returns player batting average.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		Batting average - # hits / # at-bats
	#
	#	Variables Changed:
	#		none
	#
	def get_avg(self):
		if self.ab == 0:
			return 0.0
		# Average is 0 if there are no at bats
		return float(len(self.hits)) / self.ab
	
	# get_obp:
	#	Description:
	#		Returns player on-base percentage by summing instances he got on base and
	#		dividing by plate appearances.  Plate appearances are obtained by adding
	#		at-bats, walks, hbp, errors (obtained from list of outs) and sacrifices
	#		(also obtained from list of outs).
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		On-base percentage - # times on base / plate appearances
	#
	#	Local Variables:
	#		errors - number of errors in the out list, used to calculate number of plate
	#				 appearances
	#		sacs   - number of sacrifices in the out list, used to calculate number of
	#				 plate appearances
	#	
	def get_obp(self):
		errors = 0
		sacs = 0
		for i in self.outs:
			if i.type == 'e':
				errors += 1
			elif i.type == 's':
				sacs += 1
		on_base = errors + self.walks + self.hbp + len(self.hits)
		plate_app = errors + sacs + self.ab + self.walks + self.hbp
		# OBP is 0 if there are no plate appearances
		if plate_app == 0:
			return 0.0
		return float(on_base) / plate_app
	
	# get_slg:
	#	Description:
	#		Returns player slugging percentage.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		Slugging percentage - total bases / at-bats
	#
	#	Local Variables:
	#		bases - total bases, calculated from the sum of the slug attribute for all
	#				hits in the list of hits.  Slug records bases on a hit
	#	
	def get_slg(self):
		# Slugging percentage is 0 if there are no at bats
		if self.ab == 0:
			return 0.0
		bases = 0
		for i in self.hits:
			bases += i.slug
		return float(bases) / self.ab
		
	# get_spray:
	#	Description:
	#		This takes a players information and returns a normalized array representing
	#		their spray chart by iterating through all of the hits and outs and recording
	#		where in the field they were hit to.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		spray - an array where each index is a location on the field.  Indices 0-8
	#				correspond to positions 1-9 on the field, respectively, so index 6
	#				corresponds to balls batted to position 7 on the field, or left
	#				field.  The array is normalized, so each item is between 0 and 1
	#				and they sum to 1, unless there are no data to record.
	#
	#	Local Variables:
	#		total - keeps track of total number of hits in the spray array in order to
	#				normalize in the end
	#		spray - array that increments a particular index while iterating through outs
	#				and hits if the out/hit was recorded at that position on the field
	#
	#	Shared Variables (Read-Only):
	#		outs  - each out contains data corresponding where on the field it was
	#				recorded.  We iterate through these to get the spray array
	#		hits  - each hit contains data corresponding where on the field it was
	#				recorded.  We iterate through these to get the spray array
	#
	def get_spray(self):
		# Want values in spray to be floats, so we will divide by a float
		spray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		total = 0.0
		for i in self.outs:
			spray[i.location - 1] += 1
			total += 1
		for i in self.hits:
			spray[i.location - 1] += 1
			total += 1

		# if we don't have any at bats, just return all 0's
		if total == 0:
			return spray

		for i, loc in enumerate(spray):
			spray[i] = loc / total
		return spray
			
# Team:
#	Description:
#		This class groups players onto the same team and contains the functions to save
#		and edit teams.
#
#	Attributes:
#		school:  String for name of the school
#		players: List of Players for players on the team
#
#	Functions:
#		add_player:  adds a player to the team
#		get_players: returns dictionary of Player instances indexed by full name
#		save_team:   saves the players in one file for the entire team
#
class Team:
	def __init__(self, school):
		self.school  = school
		self.players = []
		return
		
	# add_player:
	#	Description:
	#		Adds a player to the team list of players.
	#
	#	Arguments:
	#		new_guy (Player) - player to be added
	#
	#	Return Values:
	#		none
	#
	#	Variables Changed:
	#		selfplayers - player appended to list of players
	#
	def add_player(self, new_guy):
		self.players.append(new_guy)
		return

	# get_players:
	#	Description:
	#		Returns the players on the team.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		self.players
	#
	def get_players(self):
		return self.players
	
	# save_team:
	#	Description:
	#		Saves the state of the team with all of the current statistics in a .txt
	#		file with the name of the school.
	#
	#	Arguments:
	#		none
	#
	#	Return Values:
	#		none
	#	
	def save_team(self):
		team_file = open('%s.txt' %self.school, 'w')
		team_file.write('%s\n' %self.school)
		team_file.write('-' * 10 + '\n' + '-' * 10 + '\n')
		for i in self.players:
			(first, last, bat, thr, pos, grad, num) = i.get_info()
			(outs, hits, ab, walks, hbp, so) = i.get_stats()
			
			# Write personal information
			team_file.write('First:       %s\n' %first)
			team_file.write('Last:        %s\n' %last)
			team_file.write('Number:      %d\n' %num)
			team_file.write('Position(s):')
			for j in pos:
				team_file.write(' %d' % j)
			team_file.write('\nBats:        %s\n' %bat)
			team_file.write('Throws:      %s\n' %thr)
			team_file.write('Class:       %d\n' %grad)
			
			# Write stats
			team_file.write('STATS:\n')
			team_file.write('At-bats:     %d\n' %ab)
			team_file.write('Strikeouts:  %d\n' %so)
			team_file.write('Walks:       %d\n' %walks)
			team_file.write('HBP:         %d\n' %hbp)
			
			# Print non-bunt hits (bases,location) and count bunt hits
			bunts = 0
			team_file.write('Hits:       ')
			for j in hits:
				is_bunt = 0			# Want to change Boolean to 1/0
				if j.is_bunt:
					is_bunt = 1
				team_file.write(' (%d,%d,%d)' %(is_bunt, j.location, j.slug))
			team_file.write('\n')
			
			# Print out types (type,location)
			team_file.write('Outs:       ')
			for j in outs:
				team_file.write(' (%c,%d)' %(j.type, j.location))
			team_file.write('\n' + ('-' * 10) + '\n')
		team_file.close()
		return

# load_team:
#	Description:
#		This loads players into Player instances and puts them together into a Team
#		instance.
#
#	Arguments:
#		filename - A string filename in the form [school_name].txt
#
#	Return Values:
#		team - The Team instance including all of the players
#		
def load_team(filename):
	team_file = open(filename, 'r')
	line = team_file.readline().split()		# Want to remove newline character
	team = Team(line[0])					# First line contains school name
	while True:
		line = team_file.readline()
		words = line.split()
		if line == '':					# End of file
			return team
		elif len(words) > 1 and words[1] == 'None':
			continue
		elif words[0] == '-' * 10:		# Reset to add next player
			(fn, ln, bat, thr, pos, yr, num) = (None, None, None, None, None, None, None)
		elif words[0] == 'First:':
			fn = words[1]
		elif words[0] == 'Last:':
			ln = words[1]
		elif words[0] == 'Bats:':
			bat = words[1]
		elif words[0] == 'Throws:':
			thr = words[1]
		elif words[0] == 'Position(s):':
			pos = []
			for i in words[1:]:
				pos.append(int(i))
		elif words[0] == 'Class:':
			yr = int(words[1])
		elif words[0] == 'Number:':
			num = int(words[1])
		elif words[0] == 'STATS:':
			player = Player(fn, ln, bat, thr, pos, yr, num)
			team.add_player(player)
		elif words[0] == 'Hits:':
			for i, item in enumerate(words[1:]):
				chars = list(words[i + 1])
				is_bunt = False			# Want to change from 1/0 to Boolean
				if chars[1] == '1':
					is_bunt = True
				player.add_hit(True, int(chars[3]), int(chars[5]))
		elif words[0] == 'Outs:':
			for i, item in enumerate(words[1:]):
				chars = list(words[i + 1])
				player.add_out(chars[1], int(chars[3]))
		elif words[0] == 'Strikeouts:':
			for i in range(int(words[1])):
				player.add_so()
		elif words[0] == 'Walks:':
			for i in range(int(words[1])):
				player.add_walk()
		elif words[0] == 'HBP:':
			for i in range(int(words[1])):
				player.add_hbp()
	team_file.close()
		

	
