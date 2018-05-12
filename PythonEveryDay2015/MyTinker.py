# Adding Random things to a Tkinter window  
# From my brain 
# Typer: Ginny C Ghezzo 
# What I learned:  
# TODO: Need to figure out the localip return (ARG ARG)

from tkinter import * 
import time 
import urllib					# opening and reading URLs
import urllib.request			# why do I need this 
import re 						# regular expression operations 

def tick():
	global time1 
	time2 = time.strftime('%H:%M:%S')			#Convert the time to a format 
	if time2 != time1: 
		time1 = time2
		clock.config(text=time2)
	clock.after(200, tick)

def localip():
	global theIP
	url= "http://checkip.dyndns.org"
	f = urllib.request.urlopen(url).read()
	theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", str(f))
	ip.config(text=theIP)
	return theIP

def callback():
	print("click!")

root = Tk()						#This is a window 
time1 = ''
# Label is a widget to display text or graphics. Child of root 
clock = Label(root, font=('times', 20, 'bold'), bg='pink')
# pack says size yourself to the text given. fill says expand both horizontal\vertical
# pack expand assigns additional space 
clock.pack(fill=BOTH, expand=1)
ip = Label(root, font=('times', 20), bg='blue')
ip.pack(fill=BOTH, expand=1)

localip()
b = Button(root, text="EXIT", command=root.quit)
b.pack(fill=BOTH, expand=1)
tick()

#call this to draw and process events 
root.mainloop()
