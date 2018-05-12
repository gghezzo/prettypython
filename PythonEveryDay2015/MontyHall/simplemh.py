# Monty Hall and the gaot 
# Simple one pass game 
# Typer: Ginny C Ghezzo 
# What I learned: 

import random 

doors = ["A", "B", "C"]
totWins = 0 
again = 'y'

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