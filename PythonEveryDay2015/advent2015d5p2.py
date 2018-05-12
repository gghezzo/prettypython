# Advent of Code - http://adventofcode.com/day/1
# From http://adventofcode.com/day/1
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day5data.txt'
print(filename)
def checkForPairs(myStr):
    judgement = False
    i = 1
    while i < len(myStr):
        if (myStr.count(myStr[i-1:i+1]) > 1): return(True)
        i+=1
    return(judgement)
def checkForMenageatrois(myStr):
    judgement = False
    i = 2
    while i < len(myStr):
        if (myStr[i] == myStr[i-2] ): return(True)
        i += 1
    return(judgement)
def checkSantaList(myStr):
    judgement = True
    if (not checkForPairs(myStr)): return(False)
    if (not checkForMenageatrois(myStr)): return(False)
    return(judgement)

naughty = 0
nice = 0 
f = open(filename,'r')
line = f.readline()
while line: 
    if checkSantaList(line): 
        nice += 1 
    else: 
        naughty += 1
    line = f.readline()
print('Nice = ', nice, " Naughty = ", naughty)
