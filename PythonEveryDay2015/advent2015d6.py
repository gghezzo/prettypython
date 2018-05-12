# Advent of Code - http://adventofcode.com/day/3
# From http://adventofcode.com/day/3
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day6data.txt'
print(filename)

f = open(filename,'r')
r = 1000
lights = [[0 for x in range(r)] for x in range(r)]
def getX2(line):
    t = line.split()
    x = int(t[len(t) - 1].split(',')[0])
    return(x)
def getY2(line):
    t = line.split()
    y = int(t[len(t) - 1].split(',')[1])
    return(y)
def getX1(line):
    t = line.split()
    x = int(t[len(t) - 3].split(',')[0])
    return(x)
def getY1(line):
    t = line.split()
    y = int(t[len(t) - 3].split(',')[1])
    return(y)
def toggleLight(line):
    x1 = getX1(line)
    x2 = getX2(line)
    y1 = getY1(line)
    y2 = getY2(line)

    for a in range(x1,x2+1):
        for b in range(y1,y2+1):
            lights[a][b]  += 2
    return
def turnOff(line):
    x1 = getX1(line)
    x2 = getX2(line)
    y1 = getY1(line)
    y2 = getY2(line)
    for a in range(x1,x2+1):
        for b in range(y1,y2+1):
            if lights[a][b]  != 0:
                lights[a][b] = lights[a][b] - 1
    return
def turnOn(line):
    x1 = getX1(line)
    x2 = getX2(line)
    y1 = getY1(line)
    y2 = getY2(line)
    for a in range(x1,x2+1):
        for b in range(y1,y2+1):
            lights[a][b]  += 1
    return
# Maybe change this to for line in f
line = f.readline()
# Maybe change this to for line in f
while line: 
#    print("(enter)Number of 1  : ", sum(x.count(1) for x in lights))
    if 'toggle' in line: 
        toggleLight(line)
    elif 'turn off' in line:
        turnOff(line)
    elif 'turn on' in line:
        turnOn(line)
    line = f.readline()
#    print("Number of 1  : ", sum(x.count(1) for x in lights), "after ", line)
print("The end - d6 ",  "Number of 1  : ", sum(x.count(1) for x in lights))
#TODO: THis feels like it could be more pythonic :) 
bright = 0 
for i in lights: bright = bright + sum(i)
print("Brightness at end ", bright)
f.close
