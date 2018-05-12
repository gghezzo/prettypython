# Advent of Code - http://adventofcode.com/day/3
# From http://adventofcode.com/day/3
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day3data.txt'
print(filename)

f = open(filename,'r')
x =xSan=0
y = ySan=0
xRobo=0
yRobo=0
count = 0 
houses = {(x,y)} 

# Maybe change this to for line in f
while True:
    ch = f.read(1)
    if not ch: break
    elif ch == '^':
        x += 1
    elif ch == 'v':
        x -= 1
    elif ch == '>':
        y += 1
    elif ch == '<':
        y -= 1
    houses.add((x,y))
    count += 1 
    if count % 2 == 0: 
        xSan = x 
        ySan = y 
        x = xRobo
        y = yRobo
    else: 
        xRobo = x 
        yRobo = y 
        x = xSan
        y = ySan  
print(houses)
print("total homes ", len(houses) )
f.close
