# Understand Decorators 
# From https://realpython.com/blog/python/primer-on-python-decorators/
# Typer: Ginny C Ghezzo 
# What I learned: 
import sys 

def foo(bar):
	return bar + 1

def call_foo_with_arg(foo, arg):
	return foo(arg)

def parent(num):
	print("Printing from teh parent() function")
	def first_child():
		return("Print from the first_child ")
	def second_child():
		return("Print from second_child")
	try:
		assert num == 10
		return first_child
	except AssertionError:
		return second_child

def my_decorator(some_function):
	def wrapper():
		num = 10
		if num == 10: 
			print("Yes num is 10")
		else: 
			print("Not 10")
		print("   Something is happening before we call the function")
		some_function()
		print("   Someting is happening AFTER we call the function")
	return wrapper
def just_some_function():
	print("Wheee!") 

def previousExamples():
	just_some_function = my_decorator(just_some_function)
	just_some_function()

	"In Python, functions are first-class objects. "
	"This means that functions can be passed around, and used as arguments, just like any other value (e.g, string, int, float)." 
	print('Is 3 more then 2? ',foo(2)==3)
	print(foo)
	print(foo(2))
	print(type(foo))
	print('This is call with arg3 ',call_foo_with_arg(foo,3))

	"Whenever you call parent(), the sibling functions, first_child() and second_child() are also called AND because of scope, both of the sibling functions are not available (e.g., cannot be called) outside of the parent function."
	try:
		first_child()
	except: 
		print("Good Job! Don't call a function out of scope",sys.exc_info()[0])

	print ("Return Function")
	foof = parent(10)
	barb = parent(11)

	"This simply means that foo points to the first_child() function, while bar points to the second_child() function."
	print("This is just foo")
	print(foof)
	print(barb)

	print("This is the actual calls of foof and barb  ")
	print(foof())
	print(barb())

if __name__ =="__main__":
	my_decorator()

