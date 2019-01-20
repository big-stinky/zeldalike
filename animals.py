import pygame

class animals(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pyame.Suface([50,50])
		self.image.fill(255,255,255)
		self.rect = self.image.get_rect()
		self.xVelocity = 0
		self.yVelocity = 0
		self.rect[0] = 10
		self.rect[1] = 10