# name: iFixDelta.py 
# description: Identify what changed from one iFix to another 
# 

# Which version? (exm 407, 502, 602)
# Which iFixes do you want to compare? 

# Get a list of APARs in the current iFix 
# Get a list of APARs in the target iFix 
# Out put the delta setCurrent - setTarget 

import datetime 
import sys 

print('encoding = ', sys.stdout.encoding)

aparTag = '[APAR'
prodTag = '+-- Product' 
currentApars = set('')
nextApars = set('')

if len(sys.argv) > 2:
	currentName = sys.argv[1]
	nextName = sys.argv[2]
else: 
	currentName = 'CLM502iFix012readme.txt'
	nextName = 'CLM502iFix015readme.txt'

print("The Current iFix is: ", currentName)
print("The Customer is going to: ", nextName)

try: 
	currentIFix = open(currentName)
	nextIFix = open(nextName) 
except(IOError, ValueError):
	print("A file error occurred. ", currentName, nextName)
	exit()

for line in currentIFix:
	if aparTag in line: 
		currentApars.add(line)

for line in nextIFix:
	if aparTag in line: 
		nextApars.add(line)
	
print("length of current ", len(currentApars))
print("length of next ", len(nextApars))

moo = nextApars.difference(currentApars)
print("length of moo ", len(moo))
boo = list(moo)
print("length of delta ", len(boo))
print()

i = 0 

for x in boo: 
	try:
		print(i, ' + ', x)
	except UnicodeEncodeError as err:
		print("missed ", i)
		pass
	i+= 1
print(len(boo))

currentIFix.close()
nextIFix.close()
print("Fin")