# Advent of Code - http://adventofcode.com/day/2
# From http://adventofcode.com/day/2
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day2data.txt'
print(filename)

f = open(filename,'r')
floor = 0
basement = False
def getNumList(line):
    return sorted([int(i) for i in line.split('x')])

def findPaper(lenlist):
    area = 0
    h=lenlist[0]
    l=lenlist[1]
    w=lenlist[2]
    area = 3*(h*l) + 2*(h*w)+2*(l*w)
    return area
def findRibbon(lenlist): 
    volume = (2*lenlist[0]) +  (2*lenlist[1])
    perimeter = lenlist[0] * lenlist[1] * lenlist[2]
    return(volume + perimeter)
line = f.readline()
total = 0
count = 0 
ribbon = 0 
# Maybe change this to for line in f
while line: 
    count += 1
    present = getNumList(line)
    total = total+ findPaper(present)
    ribbon = ribbon + findRibbon(present)
    line = f.readline()
print("TotalSq feet of wrap ", total)
print("total presents ",count)
print("total ribbon ", ribbon)
f.close
