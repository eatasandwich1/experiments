# This function will adjust according inputs in order to properly scrape the PFF data
def simplify(x):
	x = input('What stat?: ')
	a = 0
	WRinput = [["receptions"], ["receiving yards", "yards"], ["longest reception", "longest catch"], ["targets"], ["yards per reception"], 
	["receiving touchdowns", "touchdowns", "tds"], ["longest reception", "longest catch"], ["receptions per game", "catches per game"], ["yards per game", "receiving yards per game", "ypg"],
	["catch percentage", "catch percent"], ["total yards", "yards from scrimmage", "scrimmage yards", "total yards from scrimmage"]]
	WRoutput = ["rec", "rec_yds", "rec_long", "targets", "rec_yds_per_rec", "rec_td", "rec_long", "rec_per_g", "rec_yds_per_g", "catch_pct",
	"yds_from_scrimmage"]
	# I should remove longest-related stats, they're bad for this type of graphing
	b = len(WRinput)
	# These nested loops will traverse the first array of valid inputs and change it to its proper output
	for i in range(0, b):
		c = len(WRinput[i])
		for j in range(0, c): 
			if x.lower() == WRinput[i][j]:
				x = WRoutput[i]
				a += 1
	# If no input change happened, it was an invalid input, let the user try again
	if a == 0:
		x = False
		print("Input not understood, please clarify")
	return x
