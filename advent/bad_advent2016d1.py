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

place = 0 
totalR = 0 
totalL = 0 
NS = 0
EW = 0 
for line in file:
	myline = line.rsplit(',')
for items in myline:
	try:
		item = items.strip()
		print('This is item', item, ' and 1', item[0])
		if item[0] == 'R':
			totalR += 1
			mod = (totalR % 4)
			print('Right mod', mod)
			if mod == 1:
				EW = EW + int(item[1])			# East
			elif mod == 3:
				EW = EW - int(item[1])			# West
			elif mod == 2:
				NS = NS + int(item[1])			# North
			elif mod == 0:
				NS = NS - int(item[1])			# South 
		if item[0] == 'L':
			totalL += 1 
			mod = (totalL % 4)
			print('Left mod', mod)
			if mod == 3:
				EW = EW + int(item[1])			# East
			elif mod == 1:
				EW = EW - int(item[1])			# West
			elif mod == 0:
				NS = NS + int(item[1])			# North
			elif mod == 2:
				NS = NS - int(item[1])			# South
	except: 
		print(place)
print('NS = ', NS)
print('EW = ' ,  EW)
