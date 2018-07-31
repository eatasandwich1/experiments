# This function will adjust according inputs in order to properly scrape the PFF data
def simplify(x, position):
	x = input('What stat?: ')
	a = 0
	
	# For WR/TE/HBs
	if position == "Receiving & Rushing":
		WRinput = [["receptions"], ["receiving yards", "yards"], ["longest reception", "longest catch"], ["targets"], ["yards per reception"], 
		["receiving touchdowns", "touchdowns", "tds"], ["longest reception", "longest catch"], ["receptions per game", "catches per game"], ["receiving yards per game"],
		["catch percentage", "catch percent"], ["total yards", "yards from scrimmage", "scrimmage yards", "total yards from scrimmage"], ["rushing yards", "rush yards"],
		["rush attempts", "rushes", "rushing attempts"], ["rush tds", "rushing tds", "rushing touchdowns", "rush touchdowns"], ["longest rush", "longest run"],
		["rushing yards per attempt", "rush yards per attempt", "rush ypa", "rushing ypa", "yards per rush"], ["rush yards per game", "rushing yards per game"],
		["rush attempts per game", "rushing attempts per game"]]
		
		WRoutput = ["rec", "rec_yds", "rec_long", "targets", "rec_yds_per_rec", "rec_td", "rec_long", "rec_per_g", "rec_yds_per_g", "catch_pct",
		"yds_from_scrimmage", "rush_yds", "rush_att", "rush_td", "rush_long", "rush_yds_per_att", "rush_yds_per_g", "rush_att_per_g"]
		# I should remove longest-related stats, they're bad for this type of graphing
		b = len(WRinput)
		# These nested loops will traverse the first array of valid inputs and change it to its proper output
		for i in range(0, b):
			c = len(WRinput[i])
			for j in range(0, c): 
				if x.lower() == WRinput[i][j]:
					x = WRoutput[i]
					a += 1
		

	# For QBs; same process as WR/TE/HBs	
	elif position == "Passing":
		QBinput = [["record", "wins"], ["completions", "passes completed", "pass completions"], ["attempts", "passes attempted", "pass attempts"],
		["completion percentage", "completion percentage", "completion percent"], ["passing yards", "yards", "pass yards"],
		["td", "tds", "passing tds", "pass tds", "touchdowns"], ["td percentage", "touchdown percentage", "td %", "touchdown %"], 
		["int", "ints", "passing ints", "pass ints", "interceptions"], ["int percentage", "interception percentage", "int %", "interception %"],
		["longest pass", "longest completion"], ["yards per attempt", "ypa"], ["ypc", "yards per completion"],
		["yards per game", "ypg", "passing yards per game"], ["passer rating", "rating", "qbr"], ["sacked", "times sacked"], 
		["sack yards lost", "yards lost from sacks"], ["av", "approximate value"]]
		
		QBoutput = ["qb_rec", "pass_cmp", "pass_att", "pass_cmp_perc", "pass_yds", "pass_td", "pass_td_perc", "pass_int",
		"pass_int_perc", "pass_long", "pass_yds_per_att", "pass_yds_per_cmp", "pass_yds_per_g", "pass_rating",
		"pass_sacked", "pass_sacked_yds", "av"]
		b = len(QBinput)
		for i in range(0, b):
			c = len(QBinput[i])
			for j in range(0, c):
				if x.lower() == QBinput[i][j]:
					x = QBoutput[i]
					a += 1
	
	# If no input change happened, it was an invalid input, let the user try again	
	if a == 0:
		x = False
		if position == "Passing":
			# Did this to reduce length of QBinput array
			print("Input not understood, please clarify (try not including 'qb' or 'quarterback' directly in your search)")
		else:
			print("Input not understood, please clarify")
	return x
