# Learning Python the hard way - http://learnpythonthehardway.org/book/ex13.html
# Exercise 13 -  Parameters, Unpacking, Variables   
# you get a syntax error if you do not give 3 arguments, not more , not less. 
# import will bring in modules  (like import) 
# I do not understand what the from does 
# use int() to convert 

from sys import argv
# This unpacks the variables 
script, first, second, third = argv
print "The script is called: ", script 
print "Your first variable is: ", first 
print "Your second variable is: ", second 
print "Your third variable is: ", third 

y = "What do you want to %s" % first
x = raw_input(y) 
print x 
x = raw_input("What do you want to %s" % second)
print x 