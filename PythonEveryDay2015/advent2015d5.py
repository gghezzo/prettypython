# Advent of Code - http://adventofcode.com/day/1
# From http://adventofcode.com/day/1
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day5data.txt'
print(filename)
def checkForDoubleChar(myStr): 
    judgement = False
    i=1
    # last one is broken 
    while i < len(myStr):
        if myStr[i-1] == myStr[i]: 
            return(True)
        i += 1
    
    return judgement 

def checkForVowel(myStr):
    judgement = True
    count = 0 
    count = myStr.count('a') + myStr.count('e') + myStr.count('i') + myStr.count('o') + myStr.count('u')
    if count < 3: judgement = False 
    return judgement
def checkSantaList(myStr):
    judgement = True
    if ('ab' in myStr): return(False)
    if ('cd' in myStr): return(False)
    if ('pq' in myStr): return(False)
    if ('xy' in myStr): return(False)
    if (not checkForVowel(myStr)): return(False)
    if (not checkForDoubleChar(myStr)): return(False)
    return judgement

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
