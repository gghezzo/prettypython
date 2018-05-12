# Learning Python the hard way - http://learnpythonthehardway.org/book/ex16.html
# Exercise 16 - Reading and Writing Files 


from sys import argv 
# first of the arguements is the python scripting to be run. 
script, filename = argv

print "We're going to erase %r." % filename 
print "If you don't want that, hit CTRL-C (^c)."
print "If you do want that, hit return." 

raw_input("?") 

print "Opening the file..." 
target = open(filename, 'w')

print "Truncating the file. Goodbye." 
# delete everythign in the file 
target.truncate()
print "Now I'm going to ask you for three lines."

# input stuff 
line1 = raw_input("line 1: ") 
line2 = raw_input("line 2: ") 
line3 = raw_input("line 3: ") 
oneline = line1 +"\n" + line2 + "\n" + line3 + "\n"
target.write(oneline)
target.write('old way' + '\n')
print "I'm going to write these to the file." 

# write stuff to the file and new lines 

target.write(line1) 
target.write("\n")
target.write(line2)
target.write("\n") 
target.write(line3) 
target.write("\n") 


print "And finally, we close it." 
target.close()
target = open(filename)
print target.read()
print ('\n')

