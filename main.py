import pygame

from pygame.locals import *
from pygame.sprite import Group

import actor

def main():
	clock = pygame.time.Clock()

	#initialize and prepare screen
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Zeldalike")
	
	black = 0, 0, 0

	sprites = Group()

	player = actor.Actor()

	sprites.add(player)

	#main game loop
	done = False
	while not done:
		screen.fill(black)
		sprites.draw(screen)

		pygame.display.flip()

		for e in pygame.event.get():
			if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
				done = True
				break

			if e.type == KEYUP:
				if e.key == K_RIGHT:
					player.rect.x += 10
		
		clock.tick(60)

if __name__ == '__main__':
	main()