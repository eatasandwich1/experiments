"""This program scrapes player data from the website ProFootballReference to graph some basic stats by year.
   Currently, this program only works with pure WRs, but I will expand its functions further soon.
   Made by Prashant Shankar"""

# Import necessary materials
from bs4 import BeautifulSoup
import requests
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import conditional
import summation
import exception

# Fetch a PFF link
link = input('Paste an entire ProFootballReference link here: ')
source = requests.get(link).text
soup = BeautifulSoup(source, "lxml")
	
# Print out name of player inputted
name = soup.findAll("h1", {"itemprop" : "name"})
name = [d.text for d in name]
name = "".join(map(str, name))
print("You selected:", name)

# Identify if a rusher/receiver/quarterback is found
for find_position in soup.find('h2'):
	if find_position == "Receiving & Rushing":
		print("The player selected is mainly a RB/WR/TE")
	elif find_position == "Passing":
		print("The player selected is mainly a QB")

# Search function in conditional.py
x = (False, False)
while x == (False, False):
	x = conditional.simplify(x, find_position)
statname = x[0]
realstatname = x[1]

# Give user stat options in summation.py, unless cumulative stats are unnecessary
y = False
tuple = exception.nocumulative()
if statname not in tuple:
	while y == False:
		y = summation.summation(y)
	
	
# Initialize blank array
datalist = ["blank"] * 50

# Find receiving-related stats and put on datalist array
# WARNING: Currently does not work with catch %
d = 0
for a1 in soup.findAll("tr", {"class" : "full_table"}):
	for a2 in a1.findAll("td", {"data-stat" : statname}):
		if a2.text == '':
			datalist[d] = '0'
		else:
			datalist[d] = a2.text
		d += 1
		
# Filter out empty list entries and convert from text to float
a = 0
for c in range(0, 49):
	if datalist[c] == "blank":
		a += 1
for b in range(0, a + 1):
	datalist.remove("blank")
if statname == "catch_pct":
	datalist = [item.replace("%","") for item in datalist]
datalist = list(map(float, datalist))
datalen = len(datalist)


# If no stats in category, exit program; otherwise find max value of list for later
if not datalist:
	print("No stats in selected category found! Now exiting program.")
	exit()

# If cumulative data chosen, cumulative-sum datalist	
if y == "cumulative":
	datacopy = datalist.copy()
	for d in range(1, datalen):
		datalist[d] = datalist[d] + datalist[d - 1]
print(datalist)	

#maxstat = max(datalist)
# Get year list, filter out awards/unnecessary entries, then map to integer list
statsyear = soup.findAll("th", {"data-stat" : "year_id"})
statsyear = [d.text for d in statsyear]
statsyear = [item.replace("*+","") for item in statsyear]
statsyear = [item.replace("*","") for item in statsyear]
statsyear = [item.replace("+","") for item in statsyear]
statsyear = list(filter(None, statsyear))
statsyear = [z for z in statsyear if "yr" not in z]
statsyear = [z for z in statsyear if "Year" not in z]
statsyear = [z for z in statsyear if "Career" not in z]
year = list(map(int, statsyear))

# Plot data on simple graph
plt.plot(year,datalist)
xint = range(min(year), math.ceil(max(year)) + 1)
plt.xticks(xint)
plt.suptitle(realstatname + " for " + name)
plt.show()