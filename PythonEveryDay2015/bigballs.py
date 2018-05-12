# Teaching Python Classes  by Peter Farrell 
# From http://hackingmathclass.blogspot.com/2015/08/finally-some-class.html
# Typer: Ginny C Ghezzo 
# What I learned: 

# why doesn't the first import bring in locals ?? 
import pygame 
from pygame.locals import * 
black = (0,0,0) 
white = (255,255,255) 
green = (0,255, 0) 
# ball position 
xcor = 100 
ycor = 100 

# velocity 
xvel = 2 
yvel = 1 
diameter = 20 

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Classy Balls')
done = False 						# loop until close is clicked
clock = pygame.time.Clock()			# used to manage the screen updates 
while not done: 
	for event in pygame.event.get():
		if event.type == QUIT: 
			done = True 
	screen.fill(black)
	if xcor < 0 or xcor > 600 - diameter:
		xvel = -xvel				# make it go the opposite direction 
	if ycor < 0 or ycor > 500 - diameter: 
		yvel = -yvel 
	xcor += xvel 
	ycor += yvel 

	pygame.draw.ellipse(screen, white, [xcor,ycor,diameter,diameter])
	pygame.display.update()
	clock.tick(120)
pygame.quit()