import random

#TODO: saturation for wolves

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

		#wanted veg and trees in a biome
		self.wantedVeg = 1
		self.wantedTrees = 0

		#will this creature fight members of other packs with same PACKTYPE?
		self.fightsFriend = True

		#provides meat means it gives meat to the biome per member
		self.providesMeat = 1
		
		self.aggression = 10
		self.fear = 60

		self.dead = False

	def update(self, world):
		if not self.conditionsGood():
			self.move(world)
			print("{} uh oh".format(self.name))

			self.decay += 1

			if self.decay > 3:
				self.size -= random.randrange(1, 4)
				self.decay = 0

		self.dead = self.size < 1

	def conditionsGood(self):
		biome = world.getBiome(self.x, self.y)

		return biome.veg >= self.wantedVeg and biome.trees >= self.wantedTrees

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
				self.map[y].append(Biome(random.randrange(0, 20), random.randrange(0, 20)))

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
					have_interacted.append((pack, otherPack))

					pack_fight = random.randrange(0, pack.aggression)
					otherPack_fight = random.randrange(0, otherPack.aggression)

					pack_run = random.randrange(0, pack.fear + otherPack.aggression)
					otherPack_run = random.randrange(0, otherPack.fear + pack.aggression)

					#pack devision
					if pack_fight > pack_run:
						otherPack.size -= random.randrange(1, 3)
						print("FIGHT: {}, {}".format(pack.name, otherPack.name))

					elif pack_run > pack_fight:
						pack.move(self)
						print("RUN: {}".format(pack.name))

					#other pack decision
					if otherPack_fight > otherPack_run:
						pack.size -= random.randrange(1, 3)
						print("FIGHT: {}, {}".format(otherPack.name, pack.name))

					elif otherPack_run > otherPack_fight:
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
world.packs.append(deer)
world.packs.append(deer2)

while True:	
	world.update()
	world.print()

	#for y in world:
	#	for x in world[y]:
	#		blit(rect(y * 20, x * 20, 20, 20))
#
	#for pack in worlds.pack:
	#	blit(rect(pack.x * 20, pack.y * 20, 20, 20))

	print(world.getBiome(deer.x, deer.y).meat)

	inp = input(">")