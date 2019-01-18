import pygame

class Player(pygame.sprite.Sprite):
	#initialize the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([50, 50])
		self.image.fill((255, 255, 255))

		self.rect = self.image.get_rect()

		self.xVelocity = 0
		self.yVelocity = 0

		self.rect[0] = 10
		self.rect[1] = 10

	#function to set the players velocity
	def move(self, xVel, yVel):
		self.xVelocity += xVel
		self.yVelocity += yVel

	#called on every clock cycle, changes the characters position based on velocity
	#also handles boundaries
	def update(self,mapArea,wallList):
		xOld = self.rect[0]
		xNew = xOld+self.xVelocity
		self.rect[0] = xNew

		#checks if collided with walls or map edges
		collide = pygame.sprite.spritecollide(self, wallList, False)
		if (collide or xNew >= mapArea[0]-self.rect[2] or xNew <= 0):
			self.rect[0] = xOld
			

		#y variable movement
		yOld = self.rect[1]
		yNew = yOld+self.yVelocity
		self.rect[1] = yNew

		#checks if collided with walls or map edges
		collide = pygame.sprite.spritecollide(self, wallList, False)
		if (collide or yNew >= (mapArea[1]-self.rect[3]) or yNew <= 0):
			self.rect[1] = yOld

