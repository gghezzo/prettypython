# Playing with Pygames  
# From : http://pythonprogramming.net/dashboard/#tab_games
# Typer: Ginny C Ghezzo 
# What I learned: event is SO COOL: (what event, pos, button, rel), why is 

import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0) 
blue = (0,0, 255) 
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green 
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
pygame.draw.rect(gameDisplay, red, (400, 400, 50, 25))			# x and y, width, height
pygame.draw.circle(gameDisplay, white, (150,150), 75)	#center and radius
pygame.draw.polygon(gameDisplay, green, ((25,75), (76,125), (250, 375), (400, 25), (60, 540)))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()