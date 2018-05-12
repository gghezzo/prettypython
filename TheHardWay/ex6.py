# Learning Python the hard way - http://learnpythonthehardway.org/book/ex6.html
# Exercise 6 - Strings and Text 
# creates a variable named x that is a string with a replacement 
x= "There are %d types of people." %10
# binary is a tring and do_not is a string 
binary = "binary"
do_not = "don't"
# create a new variable that combines the string 
y = "Those who know %s and those who %s." % (binary, do_not)

# straight up prints 
print x 
print y 

# straight up 
print "I said : %r" %x
print "I also said: '%s'" %y

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious 

w = "This is the left side of .... " 
e = "a string with a right side." 

print w + e 




