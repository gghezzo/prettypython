# Monty Hall and the gaot 
# From http://www.openbookproject.net/py4fun/monty/monty.html
# Typer: Ginny C Ghezzo 
# What I learned: reminder of how to use the print(str.format)

import random 
initial = input("Door A, B or C : ").upper()
action = input("Switch or Hold (S,H):").upper()
rounds = int(input("How many "))
doors = ["A", "B", "C"]
totWins = 0 
print("We will play {} times with door {}".format(str(rounds), initial))

for i in range(rounds): 
	placed = random.choice(doors)
	chosen = initial							# why? 
	used 	= [chosen, placed]					# pick the other one
	avail 	= [door for door in doors if door not in used]		#omg ... hilarious 
	opened = random.choice(avail)
	if action == "S": 
		avail = [door for door in doors if door not in [chosen, opened]]
		chosen = avail[0]
	youWin = (chosen == placed)
	if youWin : totWins += 1
	final = "  Prize placed behind", placed, "*You chose", initial, "-Opened", opened
	if action == "H" : final += "You held to ", chosen
	else: final += "You switched to", chosen
	if youWin: final += "Total wins=", str(totWins)
	print(' '.join(final))

print("Total Wins {} in {} rounds {}%".format(totWins, rounds, str((totWins/rounds)*100)))