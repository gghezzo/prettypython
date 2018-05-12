# Binary Search 
# From http://python3.codes/binary-search/ Thank you Alan Richmond 
# Typer: Ginny C Ghezzo 
# What I learned: how to use the .format on strings. 
# 

import random 
import sys 


anum = int(sys.argv[1])
size = 10 
array = random.sample(list(range(1, 20)), size)
array = sorted(array)
#array.sort()			#Why is this commented out??? 
print(anum, array)

def binary_search(number, array, lo, hi):
	if hi < lo: return -1 
	mid = (lo + hi) //2 
	if number == array[mid]:
		return mid
	elif number < array[mid]:
		return binary_search(number, array, lo, mid -1)
	else: 
		return binary_search(number, array, mid + 1, hi)

def my_search(anum, array): 
	return binary_search(anum, array, 0, len(array) - 1)

pos = my_search(anum, array)
if pos < 0: 
	print("The number was not found! Call for help! ", anum)
else: 
	print("and the winner is number {} position {} !".format(anum, pos+1) )