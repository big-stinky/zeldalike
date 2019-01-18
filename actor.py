import pygame

class Actor(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.xVelocity = 0
		self.yVelocity = 0

		self.image = pygame.Surface([50, 50])
		self.image.fill((255, 255, 255))

		self.rect = self.image.get_rect()
		
		self.rect.x = 0
		self.rect.y = 0

	def move(self, xVel, yVel):
		self.xVelocity += xVel
		self.yVelocity += yVel

	def update(self):
		self.rect.x += self.xVelocity
		self.rect.y += self.yVelocity