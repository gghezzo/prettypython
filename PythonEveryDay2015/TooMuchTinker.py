# Too much Tinker 
# From http://cseatglance.blogspot.com/2015/08/a-simple-gui-game-with-python-tkinter.html?spref=tw
# Typer: Ginny C Ghezzo 
# What I learned: 

from tkinter import * 
import random
import tkinter.messagebox

root = Tk()
Label(root, text="Find Out the Hidden Position").pack()
def findcurpos(event):
	print("You Clicked at ", event.x, event.y)
	if event.x in range(random.randint(0,130)):
		if event.y in range(80,100):
			tkinter.messagebox.showinfo("You win", "you win!!")
			print("you win")


myframe=Frame(root,bg='beige',width=130,height=130)
myframe.bind("<Button-1>", findcurpos)
myframe.pack()
root.mainloop()