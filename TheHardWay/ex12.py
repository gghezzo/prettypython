# Learning Python the hard way - http://learnpythonthehardway.org/book/ex12.html
# Exercise 12 -  prompting people  
# python variables are case sensitive 
# python -m pydoc name_of_built_in_function will give details on the function
# os does various operating system function
# sys gets you function from the interpreter (arguments, python version, stdout, stderr) 
# This is cool : http://docs.python.org/2/library/sys.html

age = raw_input("How old are you?")
height = raw_input("How tall?") 
weight = raw_input ("How much do you weigh?") 
print " You are  %r, %r, %r." % ( age, height, weight)