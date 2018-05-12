# Show PC's Time in Python's interactive mode 
# From http://gurdeepsaini11.blogspot.com/2014_11_01_archive.html
# Typer: Ginny C Ghezzo 
# What I learned: Tkinter is a GUI package, the url above is wrong ... from line 1 
# Need an exit button 

from tkinter import * 
import time 
root = Tk()				#This is a window 
time1 = ''
# Label is a widget to display text or graphics. Child of root 
clock = Label(root, font=('times', 20, 'bold'), bg='pink')
# pack says size yourself to the text given. fill says expand both horizontal\vertical
# pack expand assigns additional space 
clock.pack(fill=BOTH, expand=1)

def tick():
	global time1 
	time2 = time.strftime('%H:%M:%S')			#Convert the time to a format 
	if time2 != time1: 
		time1 = time2
		clock.config(text=time2)
	clock.after(200, tick)
tick()

#call this to draw and process events 
root.mainloop()
