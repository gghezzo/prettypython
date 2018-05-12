# Advent of Code - http://adventofcode.com/day/8 - THIS SI WRONG SOLUTION 
# From http://adventofcode.com/day/8 
# Coder : Ginny C Ghezzo 
# What I learned: This is my bad failed code. I could not figure out which \x## evaluated and which did not

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]
else: filename = 'day8data.txt'
print(filename)

file = open(filename,'r')
ofCode = 0 
ofMemory = 0
solution = 0 

for line in file:                 # Loop through each line in the data file 
    # Find the length of the line to the end? Not sure why -1 takes off the line feed
    ofCode = ofCode + len(line[:-1])
    # eval will evaluate the line through a python and thus interpret ASCII code & escapes    
    ofMemory = ofMemory + len(eval(line))          

solution = ofCode - ofMemory + 1
print("ofCode - ofMemory + 1 =", ofCode, " - ", ofMemory,"  +1 = ", solution )
# Part 2: Taken from orangut on reddit . Just the delta, not the full amount of char 
print sum(2+s.count('\\')+s.count('"') for s in open('inputs/problem8-input'))