# Monty Hall and the gaot  - GUI 
# Adding a Tkinter Gui (pass 2 )
# Typer: Ginny C Ghezzo 
# What I learned: 

import random 
from tkinter import * 
import webbrowser 

def playVideo(): 
	url = "http://9gag.com/gag/6681409" 
	webbrowser.open(url, 1)		

# todo: Wow this is crazy ugly 
# steal this http://www.python-course.eu/tkinter_entry_widgets.php
def iuGrid(root):
	Label(root, text="Which door do you pick? ").grid(row=0)
	e1 = Entry(root).grid(row=0, column=1) 
	aLabel = Label(root, text="Door 1", font=('times', 20), bg='red').grid(row=1, column=0, padx=5, pady=5)
	bLabel = Label(root, text="Door 2",font=('times', 20, 'bold'), bg='blue').grid(row=1, column=1, pady=5 )
	cLabel = Label(root, text="Door 3",font=('times', 20, 'bold'), bg='green').grid(row=1, column=2,  pady=5, padx=5)
	next = Button(root, text ="Ready?", command = playVideo).grid(row=2, columnspan =2)

doors = ["A", "B", "C"]
totWins = 0 
again = 'y'
root = Tk().wm_title("Monty Hall ")
iuGrid(root)


while again == 'y': 
	initial = input("Door A, B or C : ").upper()		# fix bad selection
	action = input("Switch or Hold (S,H):").upper()
	placed = random.choice(doors)
	chosen = initial							 
	used 	= [chosen, placed]					# pick the other one
	avail 	= [door for door in doors if door not in used]		#omg ... hilarious 
	opened = random.choice(avail)
	if action == "S": 
		avail = [door for door in doors if door not in [chosen, opened]]
		chosen = avail[0]
	youWin = (chosen == placed)
	if youWin : print("Congratulations! You win! It was in ", placed)
	else: print("Sorry it was in ", placed) 
	again = input("Do you want to play again? (y,n)").lower()

root.mainloop()