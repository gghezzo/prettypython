# Teaching Python Classes  by Peter Farrell 
# From http://hackingmathclass.blogspot.com/2015/08/finally-some-class.html
# Typer: Ginny C Ghezzo 
# What I learned: 

# why doesn't the first import bring in locals ?? 
import pygame 
from pygame.locals import * 
from random import *

black = (0,0,0) 
white = (255,255,255) 
green = (0,255, 0) 
red = (200,0, 0)
colors =[black,white,green,red]
# ball position 
xcor = 100 
ycor = 100 
class Ball():
	def __init__(self,xcor,ycor,xvel,yvel,color,diameter):
		self.xcor = xcor
		self.ycor = ycor
		self.xvel = xvel
		self.yvel = yvel 
		self.color = color 
		self.diameter = diameter
		pygame.draw.ellipse(screen, self.color, [self.xcor,self.ycor, self.diameter, self.diameter])

	def move(self): 
		if self.xcor < 0 or self.xcor > 600 - self.diameter:
			self.xvel = -self.xvel				# make it go the opposite direction 
		if self.ycor < 0  or self.ycor > 500 - self.diameter: 
			self.yvel = -self.yvel 
		self.xcor += self.xvel 
		self.ycor += self.yvel 
		pygame.draw.ellipse(screen, self.color, [self.xcor,self.ycor, self.diameter, self.diameter])


# velocity 
ball_list = []
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Big Classy Balls')
for i in range(60):
	newball = Ball(randrange(0,700), randrange(0,500), randrange(-10,10), randrange(-10,10), choice(colors), randrange(5,50,1))
	ball_list.append(newball)
	for ball in ball_list:
		ball.move()
 
done = False 						# loop until close is clicked
clock = pygame.time.Clock()			# used to manage the screen updates 
while not done: 
	for event in pygame.event.get():
		if event.type == QUIT: 
			done = True 
	screen.fill(black)
	for ball in ball_list:
		ball.move()
	pygame.display.update()
	clock.tick(120)
pygame.quit()

