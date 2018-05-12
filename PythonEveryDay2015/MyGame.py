 # Playing with Pygames  
# From : http://pythonprogramming.net/dashboard/#tab_games
# Typer: Ginny C Ghezzo 
# What I learned: event is SO COOL: (what event, pos, button, rel), why is 
#TODo: Think about the use of global pause 

import pygame
import time 
import random

pygame.init()
d_width = 800
d_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (255,100,100)
green = (0,200,0)
bright_green = (200,255,0)
blue=(0,0,255)
block_color = (53,115,255)
car_width = 73
crash_sound = pygame.mixer.Sound("crash.wav")

gameDisplay = pygame.display.set_mode((d_width,d_height))	# give me a canvas 800x600
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()							# track time in the game 
carImg = pygame.image.load('racecar.png')
gameIcon = pygame.image.load('carIcon.png')
pygame.display.set_icon(gameIcon)
pause = False

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, black)
	gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):										# class named car with a spot
	gameDisplay.blit(carImg, (x,y))					# draw an image 

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def quitgame(): 
	pygame.quit()
	quit()

def unpause():
	global pause
	pygame.mixer.music.unpause()
	pause = False

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((d_width/2),(d_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def paused():
	largeText = pygame.font.SysFont("comicsansms",115)
	TextSurf, TextRect = text_objects("Paused", largeText)
	TextRect.center = ((d_width/2),(d_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.mixer.music.pause()
	while pause:
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				pygame.quite()
				quit()
		button("Continue", 150,450, 100,50, green, bright_green, unpause)
		button("Quit", 550,450,100,50, red, bright_red, quitgame)
		pygame.display.update()
		clock.tick(15)

def crash():
	pygame.mixer.Sound.play(crash_sound)
	pygame.mixer.music.stop()
	largeText = pygame.font.SysFont("comicsansms",115)
	TextSurf, TextRect = text_objects("You Crashed", largeText)
	TextRect.center = ((d_width/2),(d_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	while True:
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				pygame.quit()
				quit()
		button("Play Again?",150, 450, 100,50, green,bright_green, game_loop)
		button("Quit",550,450,100,50, red, bright_red,quitgame)
		pygame.display.update()
		clock.tick(15)

def button(msg, x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(click)
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
		if click[0] == 1 and action !=None: 
			action()
	else: 					
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
	smallText = pygame.font.SysFont("comicsansms", 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)))
	gameDisplay.blit(textSurf,textRect)

def game_intro():
	intro = True 
	while intro: 
		for event in pygame.event.get():
			# print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',90)
		TextSurf, TextRect = text_objects("A bit Racey Intro", largeText)
		TextRect.center = ((d_width/2), (d_height/2))
		gameDisplay.blit(TextSurf, TextRect)

		button("GO!", 150,450,100,50,green, bright_green, game_loop)
		button("Quit", 550,450,100,50, red, bright_red, quitgame)
		pygame.display.update()
		clock.tick(15)

def game_loop():
	global pause
	x = (d_width * 0.45)								# starting points
	y = (d_height * 0.8)
	x_change = 0
	thing_startx = random.randrange(0,d_width) 
	thing_starty = -600
	thing_speed = 7 
	thing_width = 100
	thing_height = 100 
	thingCount = 1
	dodged = 0
	gameExit = False
	pygame.mixer.music.load('a_fallingwater.wav')
	pygame.mixer.music.play(-1)

	while not gameExit: 									# game loop 
		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_LEFT: 
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				elif event.key == pygame.K_p:
					pause = True 
					paused()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0 
		x += x_change
		gameDisplay.fill(white)						# update entire 
		things(thing_startx, thing_starty, thing_width, thing_height, black) 
		thing_starty += thing_speed

		car(x,y)
		things_dodged(dodged)
		if x > d_width - car_width or x < 0: 
			crash()									# show the changes 
		# Is the block still on the screen ? 
		if thing_starty > d_height:
			thing_starty = 0 -thing_height			# make sure it starts off screen
			thing_startx = random.randrange(0, d_width)
			dodged += 1
			thing_speed += 1 
			thing_width += (dodged * 1.2)

		if y < thing_starty+thing_height:
			# print('y crossover')
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
				# print('x crossover')
				crash()
		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()