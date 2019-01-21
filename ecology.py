import random

#TODO: var to keep track of how well they are doing
#TODO: add breeding
#TODO: add plant regrowth at fixed rate

class Biome:
	def __init__(self, veg, trees):
		self.veg = veg
		self.trees = trees
		self.meat = 0

		self.debug = False

class Pack:
	def __init__(self, name, x, y, size, packType):
		self.name = name
		
		self.x = x
		self.y = y

		self.size = size

		self.decay = 0

		#basically the animal species
		self.packType = packType

		#wanted veg and meat in a biome per member, is consumed
		self.wantedVeg = 1
		self.wantedMeat = 0

		#wanted for habitat reasons, per member
		self.wantedTrees = 0

		#will this creature fight members of other packs with same packType?
		self.fightsFriend = True

		#provides meat means it gives meat to the biome per member
		self.providesMeat = 1
		
		self.aggression = 10
		self.fear = 60

		self.damage = 1

		#number at which point the pack starts losing members if needs not met
		self.decay_max = 4

		self.dead = False

	def update(self, world):
		if not self.conditionsGood():
			self.move(world)
			print("{} uh oh".format(self.name))

			self.decay += 1

			if self.decay >= self.decay_max:
				self.size -= random.randrange(1, 4)
				self.decay = 0

		else:
			self.decay -= 1

		self.dead = self.size < 1

	def conditionsGood(self):
		biome = world.getBiome(self.x, self.y)

		return biome.veg >= self.wantedVeg * self.size and biome.trees * self.size >= self.wantedTrees and biome.meat * self.size >= self.wantedMeat

	def move(self, world):
		xMin = 0
		xMax = 0

		yMin = 0
		yMax = 0

		if self.x > 0:
			xMin = -1

		if self.x < len(world.map[0])-1:
			xMax = 2

		if self.y > 0:
			yMin = -1

		if self.y < len(world.map)-1:
			yMax = 2

		self.x += random.choice(range(xMin, xMax))
		self.y += random.choice(range(yMin, yMax))


class World:
	def __init__(self):
		self.packs = []
		self.map = []

		for y in range(5):
			self.map.append([])
			for x in range(5):
				self.map[y].append(Biome(random.randrange(0, 50), random.randrange(0, 50)))

	def update(self):
		for pack in self.packs:
			pack.update(self)

		self.packs = [pack for pack in self.packs if not pack.dead]
		
		for y in range(0, len(self.map)):
			for x in range(0, len(self.map[y])):
				biome = self.map[y][x]

				biome.meat = 0

				for pack in self.packs:
					if (pack.x, pack.y) == (x, y):
						if pack.providesMeat > 0:
							biome.meat += pack.size * pack.providesMeat
	
							print("{}: v{}, w{}".format(pack.name, biome.veg, pack.wantedVeg * pack.size))

							if biome.veg >= pack.wantedVeg * pack.size:
								biome.veg -= pack.wantedVeg * pack.size
				
							else:
								biome.veg = 0

		have_interacted = []

		#Interactions
		#Fight, Fight = both sides lose members
		#run, Fight = run loses members
		#run, run = nothing occurs, both packs leave. based on aggression

		for pack in self.packs:
			for otherPack in self.packs:
				if (pack.x, pack.y) == (otherPack.x, otherPack.y) and pack != otherPack and not (otherPack, pack) in have_interacted:
					if pack.packType == otherPack.packType and pack.fightsFriend or pack.packType != otherPack.packType:
						have_interacted.append((pack, otherPack))
	
						pack_fight = random.randrange(0, pack.aggression)
						otherPackFight = random.randrange(0, otherPack.aggression)
	
						pack_run = random.randrange(0, pack.fear + otherPack.aggression)
						otherPackRun = random.randrange(0, otherPack.fear + pack.aggression)
	
						#pack devision
						if pack_fight > pack_run:
							otherPack.size -= random.randrange(1, pack.size * pack.damage)
							print("FIGHT: {}, {}".format(pack.name, otherPack.name))
	
						elif pack_run > pack_fight:
							pack.move(self)
							print("RUN: {}".format(pack.name))
	
						#other pack decision
						if otherPackFight > otherPackRun:
							pack.size -= random.randrange(1, otherPack.size * otherPack.damage)
							print("FIGHT: {}, {}".format(otherPack.name, pack.name))
	
						elif otherPackRun > otherPackFight:
							pack.move(self)
							print("RUN: {}".format(otherPack.name))

	def print(self):
		strings = [[] for i in range(len(self.map))]

		for y in range(0, len(self.map)):			
			for x in range(0, len(self.map[y])):

				if self.map[y][x].debug:
					strings[y].append("!!")
				else:
					for pack in self.packs:
						if pack.x == x and pack.y == y:
							if pack.packType == "DEER":
								strings[y].append("DD")
								break

							elif pack.packType == "WOLF":
								strings[y].append("WW")
								break

					else:
						string = ""
						if self.map[y][x].veg > 0:
							string += "V"

						else:
							string += " "
	
						if self.map[y][x].trees > 0:
							string += "T"
	
						else:
							string += " "
		
						strings[y].append(string)

		for row in strings:
			for biome in row:
				print(biome + " ", end = "")

			print("")

	def getBiome(self, findX, findY):
		return self.map[findY][findX]

world = World()
deer = Pack("Deer1", 0, 0, 10, "DEER")
deer2 = Pack("Deer2", 0, 0, 10, "DEER")

wolf1 = Pack("Wolf1", 1, 1, 5, "WOLF")

wolf1.wantedVeg = 0
wolf1.wantedMeat = 1

wolf1.fightsFriend = False

wolf1.providesMeat = 0

wolf1.aggression = 70
wolf1.fear = 10

wolf1.damage = 2
wolf1.decay_max = 10

world.packs.append(deer)
world.packs.append(deer2)
world.packs.append(wolf1)

while True:	
	world.update()
	world.print()

	inp = input(">")