import pygame

class Wall(pygame.sprite.Sprite):

	#--------------------------------------------------------------------------
	# Creates a wall based on coordinates, dimensions and color
	#--------------------------------------------------------------------------
	def __init__(self, xCoord, yCoord, width, height, color):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([width,height])
		self.image.fill(color)
	
		self.rect = self.image.get_rect()

		# Coordinates for the wall
		self.rect[0] = xCoord
		self.rect[1] = yCoord

		# Height and width for the wall
		self.rect[2] = width
		self.rect[3] = height
