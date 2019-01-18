pop_types = {
	"DEER": 0,
	"WOLF": 1,
}

class Biome:
	def __init__(self, veg, trees):
		self.populations = []

		self.vegetation = veg
		self.trees = trees

class Population:
	def __init__(self, name, size, pop_type):
		self.name = name
		self.size = size
		self.pop_type = pop_type

class World:
	def __init__(self):
		self.world = []

		for y in range(10):
			self.world.append([])
			for x in range(10):
				self.world[y].append(Biome())

world = World()
deer = Population("Deer", 100, pop_types["DEER"])

world.populations.append(deer)