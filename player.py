import pygame

class Player(pygame.sprite.Sprite):

	#--------------------------------------------------------------------------
	# Initializes the player, and sets their size, and starting points etc.
	#--------------------------------------------------------------------------
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([50, 50])
		self.image.fill((255, 255, 255))

		self.rect = self.image.get_rect()

		self.xVelocity = 0
		self.yVelocity = 0

		self.rect[0] = 10
		self.rect[1] = 10

	#--------------------------------------------------------------------------
	# Method to change players velocity
	#--------------------------------------------------------------------------
	def move(self, xVel, yVel):
		self.xVelocity += xVel
		self.yVelocity += yVel

	#--------------------------------------------------------------------------
	# Called on every clock cycle, changes the characters position based on
	# Their velocity, also handles the map boundaries
	#--------------------------------------------------------------------------
	def update(self,mapArea,wallList):
		# X variables movement
		xOld = self.rect[0]
		xNew = xOld+self.xVelocity
		self.rect[0] = xNew

		# Checks if collided with walls or map edges
		collide = pygame.sprite.spritecollide(self, wallList, False)
		if (collide or xNew >= mapArea[0]-self.rect[2] or xNew <= 0):
			self.rect[0] = xOld
			

		# Y variable movement
		yOld = self.rect[1]
		yNew = yOld+self.yVelocity
		self.rect[1] = yNew

		# Checks if collided with walls or map edges
		collide = pygame.sprite.spritecollide(self, wallList, False)
		if (collide or yNew >= (mapArea[1]-self.rect[3]) or yNew <= 0):
			self.rect[1] = yOld

