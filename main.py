import pygame

from pygame.locals import *
from pygame.sprite import Group

import Player

def main():
	clock = pygame.time.Clock()

	#initialize and prepare screen
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Zeldalike")
	
	black = 0, 0, 0

	sprites = Group()

	player = Player.Player()

	sprites.add(player)

	#main game loop
	done = False
	while not done:
		clock.tick(60)
		screen.fill(black)
		sprites.draw(screen)


		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				done = True
				break

			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					player.move(2,0)
				if event.key == K_LEFT:
					player.move(-2,0)
				if event.key == K_UP:
					player.move(0,-2)
				if event.key == K_DOWN:
					player.move(0,2)
				

			if event.type == KEYUP:
				if event.key == K_RIGHT:
					player.move(-2,0)
				if event.key == K_LEFT:
					player.move(2,0)
				if event.key == K_UP:
					player.move(0,2)
				if event.key == K_DOWN:
					player.move(0,-2)
				
		
		player.update()

		pygame.display.flip()

if __name__ == '__main__':
	main()