import pygame

class Button(pygame.sprite.Sprite):

	#--------------------------------------------------------------------------
	# Constructor for button class, similar to the wall class
	# Takes coordinates, dimensions, and the color
	#--------------------------------------------------------------------------
	def __init__(self,x,y,width,height,color):
		self.buttonColor = color
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([width,height])
		self.image.fill(color)

		self.rect = self.image.get_rect()

		self.rect[0] = x
		self.rect[1] = y

		self.rect[2] = width
		self.rect[3] = height

		# Variables to handle if the mouse moved on or off the button
		self.oldHoverOver = False
		self.newHoverOver = False

		self.mouseUp = False
		self.mouseDown = False
		
	#--------------------------------------------------------------------------
	# Called upon each cycle, takes x and y from the mouse, as well as
	# The status of the mouse button
	#--------------------------------------------------------------------------
	def update(self,x,y,mouseOneUp,mouseOneDown):

		# A color that changes if the button is hovered over
		self.newColor = int(self.buttonColor[0]*0.6),int(self.buttonColor[1]*0.6),int(self.buttonColor[2]*0.6)

		# Changes the status of the mouse variables if the mouse has been clicked
		if mouseOneUp == True:
			self.mouseUp = True

		if mouseOneDown == True:
			self.mouseDown = True

		# Used for handling if the mouse went down on the button,
		# But then continued off the button
		if self.mouseUp == True and self.mouseDown == False:
			self.mouseUp = False
			self.mouseDown = False

		# If statements that handle if the button was hovered over
		if (x>= self.rect[0]) and (x <= self.rect[0] + self.rect[2]):
			if (y>= self.rect[1]) and (y <= self.rect[1] + self.rect[3]):  
				self.image.fill(self.newColor)
				self.newHoverOver = True				
			else:
				self.image.fill(self.buttonColor)
				self.newHoverOver = False
		else:
			self.image.fill(self.buttonColor)
			self.newHoverOver = False

		# This needs to be inbetween setting the newHoverOver
		# And setting the oldHoverOver
		# This handles if the mouse moved off the button, or moved
		# On the button and sets the mouse values appropriately
		if self.oldHoverOver != self.newHoverOver:
			self.mouseDown = False
			self.mouseUp = False

		# Sets oldHoverOver to newHoverOver, and returns if the 
		# Button got clicked		
		if (self.newHoverOver == True and self.mouseUp == True and self.mouseDown == True):
			self.oldHoverOver = self.newHoverOver
			return True
		else:
			self.oldHoverOver = self.newHoverOver
			return False
		