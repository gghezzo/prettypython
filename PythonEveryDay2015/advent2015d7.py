# Advent of Code - http://adventofcode.com/day/3
# From http://adventofcode.com/day/3
# Coder : Ginny C Ghezzo 
# What I learned: 

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day6data.txt'
if len(sys.argv) > 2:
    letter = sys.argv[2]
else: letter = 'a'
print(filename)
print(letter)

f = open(filename,'r')
line = f.readline()
mindstorm = {}
def isInt(x):
    try: 
        int(x)
        return(True)
    except: 
        return(False)
def updateValue(key):
    if isInt(key): return(int(key))          #just a number 
    action = mindstorm[key]
    if isInt(action):
        mindstorm[key] = int(action)    #not sure if this is needed      
        return(int(action))
    else: 
        a = action.split(' ')
        if 'NOT' in a:     # This is the NOT case 
            t = ~(updateValue(a[1]))        #Take the value of the not  as a key and find its int 
        elif 'AND' in a: 
            t = (updateValue(a[0])) & (updateValue(a[2]))
        elif 'OR' in a: 
            t = (updateValue(a[0])) | (updateValue(a[2]))
        elif 'LSHIFT' in a: 
            t = (updateValue(a[0]) << int(a[2]))
        elif 'RSHIFT' in a: 
            t = (updateValue(a[0]) >> int(a[2]))
        else:
            t = updateValue(a[0])
        mindstorm[key] = int(t)    #not sure if this is needed   
        return(int(t))
    return()
while line: 
    key = line.split('->')[1].rstrip().lstrip()
    action = line.split('->')[0].lstrip()
    if key not in mindstorm: 
        mindstorm[key] = action
    line = f.readline()
print("The value of ", letter)
print(updateValue(letter))
f.close
