# Provides a random float between 0 and 1  
# From http://code.activestate.com/recipes/579072-examples-for-random-float-between-0-and-1/?in=lang-python
# Typer: Ginny C Ghezzo 
# What I learned:

 import os 					# portable way to get to OS dependent functionality 
 import struct 				# converts between Python values an C structs (ugh) 

def random_1():
	return(int.from_bytes(os.urandom(7), 'big') >> 3) * 2 ** -53

def random_2():
	return(int.from_bytes(os.urandom(7), 'big') >> 3) / (1 <<53)

def random_3():
	array = bytearray(b'x3F' + os.urandom(7))
	array[1] |= 0xF0
	return struct.unpack('>d', array) [0] - 1
	
