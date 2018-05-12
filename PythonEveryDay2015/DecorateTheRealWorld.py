# "Real World" example of Decorators 
# From https://realpython.com/blog/python/primer-on-python-decorators/
# Typer: Ginny C Ghezzo 
# What I learned: The flask stuff never worked 

import time 
from time import sleep 
from functools import wraps
from flask import g, request, redirect, url_for, Flask
def timing_function(some_function):
	#Outputs the time a function takes to execute 
	def wrapper():
		t1 = time.time()
		some_function()
		t2 = time.time()
		return "Time it took to run the function: " + str((t2-t1)) + "\n"
	return wrapper

@timing_function
def my_function():
	num_list = []
	for x in (range(0,10000)):
		num_list.append(x)
	print("\nSum of all the numbers: " + str((sum(num_list))))

def sleep_decorator(function):
	# limits how fast the function is called 
	def wrapper(*args, **kwargs):
		sleep(2)
		return function(*args,**kwargs)
	return wrapper 

@sleep_decorator
def print_number(num):
	return num 

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None: 
			return redirect(url_for('login', next=request.url))
		return f(*args, **kwargs)
	return decorated_function

app = Flask(__name__)

@app.route('/secret')
@login_required
def secret():
	print("Hmmm is this doing anything?")

print(my_function())
print(print_number(222))
'''
print(secret())
for x in range(1,6):
	print(print_number(x)
'''