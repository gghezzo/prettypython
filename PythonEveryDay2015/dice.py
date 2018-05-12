# Graphical Dice 
# From http://python3.codes/a-graphical-dice-simulator/  
# Typer: Ginny C Ghezzo 
# What I learned: more about pip install, how to download pygames, .whl,  
# TODO: It is ugly, fix this. 
# TODO: Prompt to exit 

# Simpliest possible dice 
import random 
print(random.randint(1,6))

# Alan Richmon's pretty version 
import pygame, time 

size = 256
spsz = size//10			# size of a spot 
m = int(size/2)			# middle 
l=t=int(size/4)			# left and top 
r=b=size-1				# right and bottom 
rolling = 12 			# times to roll (https://www.youtube.com/watch?v=N9qYF9DZPdw) 
diecol = (255,255,127)	# die color 
spotcol = (0, 127, 127)	# spot color 

d=pygame.display.set_mode((size, size))
d.fill(diecol)
pygame.display.set_caption("Andrew Dice Simulator")

for i in range(rolling):
	n=random.randint(1,6)
	print(n)
	d.fill(diecol)
	if n % 2 == 1: 
		pygame.draw.circle(d, spotcol, (m,m), spsz) 
	if n==2 or n==3 or n==4 or n==5 or n==6: 
		pygame.draw.circle(d, spotcol, (l,b), spsz)
		pygame.draw.circle(d, spotcol, (r,t), spsz)
	if n==4 or n==5 or n==6:
		pygame.draw.circle(d, spotcol, (l,t), spsz)
		pygame.draw.circle(d, spotcol, (r,b), spsz)
	if n==6: 
		pygame.draw.circle(d, spotcol, (m,b), spsz)
		pygame.draw.circle(d, spotcol, (m,t), spsz)
	pygame.display.flip()
	time.sleep(1)				# in seconds 