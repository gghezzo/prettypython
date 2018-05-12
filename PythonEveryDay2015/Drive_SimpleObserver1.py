# Using the Observer Pattern from SimpleObserver 
# From https://newcircle.com/s/post/1743/2015/06/17/tutorial-the-observer-pattern-in-python?utm_campaign=YouTube_Channel&utm_source=youtube&utm_medium=social&utm_content=Observer%20Pattern%20in%20Python%20Tutorial%20-%20Description
# Typer: Ginny C Ghezzo 
# What I learned: The import is amusingly case sensitive 

from SimpleObserver import Publisher, Subscriber
pub = Publisher()
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John') 

pub.register(bob)
pub.register(alice)
pub.register(john) 

pub.dispatch("It is Lunchtime! ")

pub.unregister(john)
pub.dispatch("Time for Dinner dearies")


