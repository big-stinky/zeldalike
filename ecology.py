import random

packTypes = {
	"DEER": 0,
	"WOLF": 1,
}

class Biome:
	def __init__(self, veg, trees):
		self.veg = veg
		self.trees = trees
		self.meat = 0

class Pack:
	def __init__(self, name, x, y, size, packType):
		self.name = name
		
		self.x = x
		self.y = y

		self.size = size
		self.packType = packType

		self.decay = 0

	def update(self, world):
		if not self.conditions_good():
			self.move(world)

			self.decay += 1

			if self.decay > 0:
				self.size -= random.randrange(1, 4)
				print("decay")
				self.decay = 0

	def conditions_good(self):
		return world.get_biome(self.x, self.y).veg > 1

	def move(self, world):
		x_min = self.x
		x_max = self.x

		y_min = self.y
		y_max = self.y

		if self.x > 0:
			x_min = self.x-1

		if self.x < len(world.map[0]):
			x_max = self.x+2

		if self.y > 0:
			y_min = self.y-1;

		if self.y < len(world.map)-1:
			y_max = self.y+2

		self.x = random.choice(range(x_min, x_max))
		self.y = random.choice(range(y_min, y_max))


class World:
	def __init__(self):
		self.packs = []
		self.map = []

		for y in range(5):
			self.map.append([])
			for x in range(5):
				self.map[y].append(Biome(0, 0))

	def print(self):
		for y in range(0, len(self.map)):
			print("")
			for x in range(0, len(self.map[y])):
				for pack in self.packs:
					if pack.x == x and pack.y == y:
						if pack.packType == packTypes["DEER"]:
							print("DD ", end = "")
							break

				else:
					print("{}{} ".format(self.map[y][x].veg, self.map[y][x].trees), end = "")

		print()

	def get_biome(self, find_x, find_y):
		for y in range(0, len(self.map)):
			for x in range(0, len(self.map[y])):
				if (x, y) == (find_x, find_y):
					return self.map[y][x]

		return False

world = World()
deer = Pack("Deer", 0, 0, 100, packTypes["DEER"])
world.packs.append(deer)

while True:	
	world.print()
	inp = input(">")
	
	deer.update(world)