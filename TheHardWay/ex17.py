# Learning Python the hard way - http://learnpythonthehardway.org/book/ex17.html
# Exercise 17 - More Files

print("This takes two parameters from and to file") 
# we are going to use two methods from sys and os 
from sys   argv 
from os.path import exists 

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file) 

# we could do these two on one line too, how ? 
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata) 
print "Does the output file exist? %r" % exists(to_file) 
print "Ready, hit Return to continue, ctrl-c to abort."
raw_input()

out_file = open(to_file, 'w') 
out_file.write(indata) 

print "Alright, all done" 

out_file.close()
in_file.close()
