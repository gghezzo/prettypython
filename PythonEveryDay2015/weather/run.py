# Trying to do Flask 
# From my brain - https://www.twilio.com/docs/quickstart/python/devenvironment#debugging-errors 
# Typer: Ginny C Ghezzo 
# What I learned: Twilio and Flask 

from flask import Flask, request, redirect
import twilio.twiml 

app = Flask(__name__)

# @app.route("/", methods=['GET','POST'])
@app.route("/")
def hello_monkey():
	"""Respond to incoming calls with a simple text message."""
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey")
	return str(resp)
	
def hello():
	return "Hello World! "

@app.route('/<name>')
def hello(name):
	return "Hello {}! ".format(name)
	

if __name__ == "__main__":
	app.run(debug=True) 