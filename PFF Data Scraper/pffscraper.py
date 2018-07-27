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

# Fetch a PFF link
link = input('Paste an entire ProFootballReference link here: ')
source = requests.get(link).text
soup = BeautifulSoup(source, "lxml")

# Print out name of player inputted
name = soup.findAll("h1", {"itemprop" : "name"})
name = [d.text for d in name]
name = "".join(map(str, name))
print("You selected:", name)


# Search function in conditional.py
x = False
while x == False:
	x = conditional.simplify(x)

# Initialize blank array
datalist = [None] * 50

# Find receiving-related stats and put on datalist array
# WARNING: Currently does not work with catch %
d = 0
for a1 in soup.findAll("tr", {"class" : "full_table"}):
	for a2 in a1.findAll("td", {"data-stat" : x}):
		datalist[d] = a2.text
		d += 1

# Filter out empty list entries and convert from text to float
datalist = list(filter(None, datalist))
datalist = list(map(float, datalist))

# If no stats in category, exit program; otherwise find max value of list for later
if not datalist:
	print("No stats in selected category found! Now exiting program.")
	exit()
maxstat = max(datalist)

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
plt.plot(year,datalist, 'ro')
xint = range(min(year), math.ceil(max(year)) + 1)
plt.xticks(xint)
plt.show()
