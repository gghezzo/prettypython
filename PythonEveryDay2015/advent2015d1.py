# Advent of Code - http://adventofcode.com/day/1
# From http://adventofcode.com/day/1
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day1data.txt'
print(filename)

f = open(filename,'r')
floor = 0
basement = False
while True:
    ch = f.read(1)
    if not ch: break
    elif ch == '(':
    	floor += 1
    elif ch == ')':
        floor -=1
        if floor < 0 and basement == False: 
        	basement = True
        	print(f.tell())


print(floor)
