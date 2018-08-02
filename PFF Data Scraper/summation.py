# This function asks whether the user wants cumulative data or year-by-year basis data.
def summation(y):
	y = input("Do you want 'year by year' stats or 'cumulative' stats?: ")
	if y == "year by year":
		return y
	elif y == "cumulative":
		return y
	# If invalid input, prompt the user again
	else:
		y = False
		print("Input not understood, please type 'year by year' or 'cumulative'")
		return y