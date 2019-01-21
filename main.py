import pygame

from pygame.locals import *
from pygame.sprite import Group

import player, wall, button

mapArea = [800,600]
width = mapArea[0]
height = mapArea[1]


# Global variables to control different "scenes"
global titleScreen, gameScreen, optionsScreen


titleScreen = True
gameScreen = False
optionsScreen = False

#--------------------------------------------------------------------------
# Main method to swap between different scenes
#--------------------------------------------------------------------------
def main():
	global titleScreen, gameScreen, optionsScreen
	pygame.init()
	screen = pygame.display.set_mode((mapArea[0], mapArea[1]))
	pygame.display.set_caption("Zeldalike")
	
	while True:
		if titleScreen == True:
			titleLoop(screen)

		if gameScreen == True:
			gameLoop(screen)

		if optionsScreen == True:
			optionsLoop(screen)

#--------------------------------------------------------------------------
# Game Scene which will handle gameplay mechanics on the screen
#--------------------------------------------------------------------------
def gameLoop(screen):
	clock = pygame.time.Clock()

	global gameScreen


	black = 0, 0, 0

	# Moving sprites group
	movingSprites = Group()
	playerSprite = player.Player()
	movingSprites.add(playerSprite)

	# Group which contains the wall class
	walls = Group()
	newWall = wall.Wall(150,200,50,50,(255,255,0))
	walls.add(newWall)
	newWall = wall.Wall(50,200,32,32,(2,255,0))
	walls.add(newWall)
	newWall = wall.Wall(250,200,64,64,(255,25,0))
	walls.add(newWall)
	
	while gameScreen:

		clock.tick(60)
		screen.fill(black)
		movingSprites.draw(screen)
		walls.draw(screen)

		# Basic event if statement block
		for event in pygame.event.get():

			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				gameScreen = False
				quit()

			if event.type == KEYDOWN:
				if event.key == K_RIGHT or event.key == K_d:
					playerSprite.move(2,0)
				if event.key == K_LEFT or event.key == K_a:
					playerSprite.move(-2,0)
				if event.key == K_UP or event.key == K_w:
					playerSprite.move(0,-2)
				if event.key == K_DOWN or event.key == K_s:
					playerSprite.move(0,2)

			if event.type == KEYUP:
				if event.key == K_RIGHT or event.key == K_d:
					playerSprite.move(-2,0)
				if event.key == K_LEFT or event.key == K_a:
					playerSprite.move(2,0)
				if event.key == K_UP or event.key == K_w:
					playerSprite.move(0,2)
				if event.key == K_DOWN or event.key == K_s:
					playerSprite.move(0,-2)
				
		
		playerSprite.update([width,height],walls)

		pygame.display.flip()

#--------------------------------------------------------------------------
# Main loop which controls the title screen
#--------------------------------------------------------------------------
def titleLoop(screen):

	global titleScreen, gameScreen, optionsScreen

	clock = pygame.time.Clock()

	# Creating a font with size 15, and color (255,0,0)
	font = pygame.font.SysFont('Comic Sans MS', 15)
	text = font.render("ZeldaLike", 1, (255,0,0))

	# Group for each button
	buttons = Group()
	startButton = button.Button(50,50,50,50,(200,200,200))
	buttons.add(startButton)
	optionsButton = button.Button(50,200,50,50,(25,255,100))
	buttons.add(optionsButton)

	titleScreenColor = 255,200,200

	# Setting the mouse button variables
	mouseDown = False
	mouseUp = False

	while titleScreen:

		screen.fill(titleScreenColor)

		buttons.draw(screen)

		# Puts the text on the screen
		screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

		mouseX = pygame.mouse.get_pos()[0]
		mouseY = pygame.mouse.get_pos()[1]

		# Event block
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			if event.type == MOUSEBUTTONDOWN:
				mouseDown = True
			else:
				mouseDown = False

			if event.type == MOUSEBUTTONUP:
				mouseUp = True
			else:
				mouseUp = False

		# Updates the boolean if any button was clicked
		startButtonClicked = startButton.update(mouseX,mouseY,mouseUp,mouseDown)
		optionsButtonClicked = optionsButton.update(mouseX,mouseY,mouseUp,mouseDown)


		# Triggers what happens when a button is pressed
		if startButtonClicked == True:
			titleScreen = False
			gameScreen = True

		if optionsButtonClicked == True:
			print("click o")
			titleScreen = False
			optionsScreen = True



		pygame.display.flip()
		clock.tick(60)

#--------------------------------------------------------------------------
# Main method to test different scenes going back and forth
#--------------------------------------------------------------------------
def optionsLoop(screen):
	global titleScreen,optionsScreen

	clock = pygame.time.Clock()

	font = pygame.font.SysFont('Comic Sans MS', 15)
	text = font.render("Options Screen", 1, (255,0,0))

	buttons = Group()
	backButton = button.Button(50,50,50,50,(200,200,200))
	buttons.add(backButton)

	optionsScreenColor = 100,200,200

	mouseDown = False
	mouseUp = False

	while optionsScreen:

		screen.fill(optionsScreenColor)

		buttons.draw(screen)

		screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

		mouseX = pygame.mouse.get_pos()[0]
		mouseY = pygame.mouse.get_pos()[1]


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			if event.type == MOUSEBUTTONDOWN:
				mouseDown = True
			else:
				mouseDown = False

			if event.type == MOUSEBUTTONUP:
				mouseUp = True
			else:
				mouseUp = False


		backButtonClicked = backButton.update(mouseX,mouseY,mouseUp,mouseDown)
		
		if backButtonClicked == True:
			optionsScreen = False
			titleScreen = True

		pygame.display.flip()
		clock.tick(60)


if __name__ == '__main__':
	main()