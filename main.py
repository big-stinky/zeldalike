import random, math, pygame
from pygame.locals import *

def main():
	"This is the starfield code"
	#create our starfield
	random.seed()
	clock = pygame.time.Clock()

	#initialize and prepare screen
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Zeldalike")
	
	white = 255, 240, 200
	black = 20, 20, 40
	
	screen.fill(black)

	#main game loop
	done = False
	while not done:
		pygame.draw.rect(screen, white, pygame.Rect(0, 0, 40, 30))
		pygame.display.update()

		for e in pygame.event.get():
			if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
				done = 1
				break
		
		clock.tick(60)

if __name__ == '__main__':
	main()