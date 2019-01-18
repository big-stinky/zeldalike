import random

#TODO: saturation for wolves

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

		self.wanted_veg = 1
		self.wanted_trees = 0

		self.dead = False

	def update(self, world):
		if not self.conditions_good():
			self.move(world)

			self.decay += 1

			if self.decay > 3:
				self.size -= random.randrange(1, 4)
				self.decay = 0

		self.dead = self.size < 1

	def conditions_good(self):
		biome = world.get_biome(self.x, self.y)

		return biome.veg >= self.wanted_veg and biome.trees >= self.wanted_trees

	def move(self, world):
		x_min = 0
		x_max = 0

		y_min = 0
		y_max = 0

		if self.x > 0:
			x_min = -1

		if self.x < len(world.map[0])-1:
			x_max = 2

		if self.y > 0:
			y_min = -1

		if self.y < len(world.map)-1:
			y_max = 2

		self.x += random.choice(range(x_min, x_max))
		self.y += random.choice(range(y_min, y_max))


class World:
	def __init__(self):
		self.packs = []
		self.map = []

		for y in range(5):
			self.map.append([])
			for x in range(5):
				self.map[y].append(Biome(random.randrange(0, 20), random.randrange(0, 20)))

	def update(self):
		for pack in self.packs:
			pack.update(self)

		self.packs = [pack for pack in self.packs if not pack.dead]

		for pack in self.packs:
			biome = self.get_biome(pack.x, pack.y)
	
			if pack.packType == packTypes["DEER"]:
				if biome.veg >= pack.wanted_veg * pack.size:
					biome.veg -= pack.wanted_veg * pack.size
	
				else:
					biome.veg = 0

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
					if self.map[y][x].veg > 0:
						print("V", end = "")

					else:
						print(" ", end = "")

					if self.map[y][x].trees > 0:
						print("T", end = "")

					else:
						print(" ", end = "")

					print(" ", end = "")
		print()

	def get_biome(self, findX, findY):
		for y in range(0, len(self.map)):
			for x in range(0, len(self.map[y])):
				if (x, y) == (findX, findY):
					return self.map[y][x]

		return False

world = World()
deer = Pack("Deer", 0, 0, 10, packTypes["DEER"])
world.packs.append(deer)

while True:	
	world.print()

	inp = input(">")
	
	world.update()