# Advent of Code - http://adventofcode.com/day/4
# From http://adventofcode.com/day/4
# Coder : Ginny C Ghezzo 
# What I learned: about hashlib and MD5

import sys
import hashlib
if len(sys.argv) > 1:
	key = sys.argv[1]
else: key = 'ckczppom'
print(key)
count = 1 

# Maybe change this to for line in f
while True:
    # create a hash, check if 1st 5 characters are '00000' break other wise increment 
    b = bytes(key+str(count), 'utf-8')
    m = hashlib.md5(b)
    if m.hexdigest()[:6] == '000000': 
        break
    else:
        count += 1
    
print("Count ", count )
