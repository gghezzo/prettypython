# Learning Python the hard way - http://learnpythonthehardway.org/book/ex18.html
# Exercise 18 - Names, Variables, Code, Function 
# start with def, name only char or _, open parm, arguments, close parm and :,  
# new line , four indent, end by no indent 

# this one is like your scripts with argv 
# colon has to be at the end.  Next an indent 4 spaces 
def print_two(*args): 
	arg1, arg2 = args 
	print "arg1: %r, arg2: %r" % (arg1, arg2) 
	
# ok that *args is actually pointless, we can just do this 
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2) 
	
#this just takes one argument 
def print_one(arg1):
	print "arg1: %r" % arg1 
	
# this one takes no arguements 
def print_none():
	print "I got nothin;." 
	
print_two("uno", "dos")
print_two_again("111", "222") 
print_one("First!") 
print_none() 