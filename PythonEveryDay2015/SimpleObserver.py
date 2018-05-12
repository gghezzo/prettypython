# The classes of the Observer Pattern (observe1.py in the example)
# From https://newcircle.com/s/post/1743/2015/06/17/tutorial-the-observer-pattern-in-python?utm_campaign=YouTube_Channel&utm_source=youtube&utm_medium=social&utm_content=Observer%20Pattern%20in%20Python%20Tutorial%20-%20Description
# Typer: Ginny C Ghezzo 
# What I learned: 
# Todo: Think more about the describtion above. What is this file really 

class Subscriber: 
	def __init__(self, name):
		self.name = name
	def update(self, message):
		print('{} got message "{}"'.format(self.name, message))

class Publisher: 
	def __init__(self):
		self.subscribers = set()
	def register(self, who):
		self.subscribers.add(who)
	def unregister(self, who):
		self.subscribers.discard(who)
		print("Good-bye {}".format(str(who.name)))

	def dispatch(self, message):
		for subscriber in self.subscribers:
			subscriber.update(message)


