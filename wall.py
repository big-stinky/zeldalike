import pygame

class Wall(pygame.sprite.Sprite):
	#constructor, takes coordinates and wall size
	def __init__(self, xCoord, yCoord, width, height, color):
		#pygame.sprite.Sprite.__init__(self)
		super().__init__()

		self.image = pygame.Surface([width,height])
		self.image.fill(color)
	
		self.rect = self.image.get_rect()

		#coordinates for the wall
		self.rect[0] = xCoord
		self.rect[1] = yCoord

		#height and width for the wall
		self.rect[2] = width
		self.rect[3] = height
