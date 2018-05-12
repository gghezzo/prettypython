 
# TKinter example and some Graphics 
# From http://code.activestate.com/recipes/579052-animated-raster-graphics-demo-in-tkinter/
# Typer: Ginny C Ghezzo 
# What I learned: Funny assignment, ; will let you put two lines on one (boo)
# What I did: The code on line is a little wrong. I debugged it! 
# Very fullfilling (wrong indentation, did not reference self.cs, did not cast to int)
# Issues: does not launch directly from windows

import tkinter
from math import sin, cos
from random import randint 
x,y=320,200							#Annoying assingment 

class App:
	def __init__(self, t):
		self.img = tkinter.PhotoImage(width=x, height=y)
		self.c = tkinter.Label(t,image=self.img); self.c.pack()
		t.after_idle(self.do_rotozoom)

	def do_rotozoom(self):
		self.ang=int((self.ang+1)%100)			# huh
		cs1=self.cs[self.ang]					# huh
		ss1=self.ss[self.ang]
		self.img.put((" ".join((("{"+" ".join(clr[((i+cs1-j*ss1) & (j*cs1+i*ss1))//256]
			for i in range(-160,159)))+"}" for j in range(-100,99)))))
		t.after(20,self.do_rotozoom)

	#precalculate trip 
	cs, ss, ang=[], [], 0
	for i in range(100): 
		aa=abs(sin(ang))*255
		cs.append(int(cos(ang)*aa))
		ss.append(int(sin(ang)*aa))
		ang+=0.062832

	#precalculate a black/white color table 
clr=[]
for i in range(256):
	clr.append( "#{:06x}".format(i*0x10101))

t=tkinter.Tk()
a = App(t )
t.mainloop()
