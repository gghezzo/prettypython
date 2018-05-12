# Advent of Code - Day 1 - No Time for a Taxicab http://adventofcode.com/2016/day/1
# From http://adventofcode.com/2016/day/1
# Typer  : Ginny C Ghezzo 
# Given the input of R#, L# how far is the HQ ? 

# Read in the data 
# Loop through the enteries, pull out the number, 

import sys						# file 
if len(sys.argv) > 1:
    filename = sys.argv[1]
else: filename = 'day1data16.txt'
file = open(filename,'r')
print(filename)

rights = 0
lefts = 0 
place = 0 
for line in file:
	myline = line.rsplit(',')
for items in myline:
	item = items.strip()
	print('item = ', item)
	try:
		if item[0] == 'R':
			rights += 1 
		if item[0] == 'L':
			lefts += 1 
		if item[0] == lastDir: 
			print('Hey ', item[0])
			place = place - int(item[1])
		else: 
			print('Hey ', item[0])
			place = place + int(item[1])
			lastDir = item[0]
	except: 
		print(place)
print(place)