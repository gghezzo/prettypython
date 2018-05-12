# Learning Python the hard way - http://learnpythonthehardway.org/book/ex11.html
# Exercise 11 -  asking questions 
# note input opens up a security issue because you can use dir () and see the variables
# see this http://www.wellho.net/mouth/956_Python-security-trouble-with-input.html
# what does dir() do?  It lists all the local scope variables 

print "How old are you?", 
age = raw_input()
print "How tall are you?", 
height = raw_input()
print "How much do you weigh?", 
weight = input()

print "So you are %r old, %r tall and %r heavy." % (
	age,  height, weight)

x = weight - 10
print "If you lose 10 pounds you will weight %r" %(x) 
	