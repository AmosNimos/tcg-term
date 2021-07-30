from random import choice

## 

## Cards class
class Creature:

	tapped = False;
	kind = ""; # Human, Dinosaur Avatar, Vampire...
	cost = cost;
	total_cost = total_cost;
	name = ""
	power = power;
	taughness = taughness;
	type_line = ""
	rarity = "common"

	# fix value
	creature_rarity = ["common","uncomon","rare","mythic rare"]
	creature_kinds = ["Advisor", "Aetherborn", "Ally", "Angel", "Anteater",
	"Antelope", "Ape", "Archer", "Archon", "Artificer", "Assassin", "Assembly-Worker",
    "Atog", "Aurochs", "Avatar", "Badger", "Barbarian", "Basilisk", "Bat", "Bear", "Beast",
    "Beeble", "Berserker", "Bird", "Blinkmoth", "Boar", "Bringer", "Brushwagg", "Camarid",
    "Camel", "Caribou", "Carrier", "Cat", "Centaur", "Cephalid", "Chimera", "Citizen", "Cleric",
    "Cockatrice", "Construct", "Coward", "Crab", "Crocodile", "Cyclops", "Dauthi", "Demon", "Deserter",
    "Devil", "Dinosaur", "Djinn", "Dragon", "Drake", "Dreadnought", "Drone", "Druid", "Dryad", "Dwarf", 
    "Efreet", "Elder", "Eldrazi", "Elemental", "Elephant", "Elf", "Elk", "Eye", "Faerie", "Ferret", "Fish", 
    "Flagbearer", "Fox", "Frog", "Fungus", "Gargoyle", "Germ", "Giant", "Gnome", "Goat", "Goblin", "God", 
    "Golem", "Gorgon", "Graveborn", "Gremlin", "Griffin", "Hag", "Harpy", "Hellion", "Hippo", "Hippogriff", 
    "Hormarid", "Homunculus", "Horror", "Horse", "Hound", "Human", "Hydra", "Hyena", "Illusion", "Imp", 
    "Incarnation", "Insect", "Jellyfish", "Juggernaut", "Kavu", "Kirin", "Kithkin", "Knight", "Kobold", 
    "Kor", "Kraken", "Lamia", "Lammasu", "Leech", "Leviathan", "Lhurgoyf", "Licid", "Lizard", "Manticore", 
    "Masticore", "Mercenary", "Merfolk", "Metathran", "Minion", "Minotaur", "Mole", "Monger", "Mongoose", 
    "Monk", "Moonfolk", "Mutant", "Myr", "Mystic", "Naga", "Nautilus", "Nephilim", "Nightmare", "Nightstalker", 
    "Ninja", "Noggle", "Nomad", "Nymph", "Octopus", "Ogre", "Ooze", "Orb", "Orc", "Orgg", "Ouphe", "Ox", "Oyster", 
    "Pegasus", "Pentavite", "Pest", "Phelddagrif", "Phoenix", "Pincher", "Pirate", "Plant", "Praetor", "Prism", 
    "Processor", "Rabbit", "Rat", "Rebel", "Reflection", "Rhino", "Rigger", "Rogue", "Sable", "Salamander", "Samurai", 
    "Sand", "Saproling", "Satyr", "Scarecrow", "Scion", "Scorpion", "Scout", "Serf", "Serpent", "Shade", "Shaman", 
    "Shapeshifter", "Sheep", "Siren", "Skeleton", "Slith", "Sliver", "Slug", "Snake", "Soldier", "Soltari", "Spawn", 
    "Specter", "Spellshaper", "Sphinx", "Spider", "Spike", "Spirit", "Splinter", "Sponge", "Squid", "Squirrel", "Starfish", 
    "Surrakar", "Survivor", "Tetravite", "Thalakos", "Thopter", "Thrull", "Treefolk", "Triskelavite", "Troll", "Turtle", 
    "Unicorn", "Vampire", "Vedalken", "Viashino", "Volver", "Wall", "Warrior", "Weird", "Werewolf", "Whale", "Wizard", 
    "Wolf", "Wolverine", "Wombat", "Worm", "Wraith", "Wurm", "Yeti", "Zombie", "Zubera"]

	def gen_creature():
		self.name = namegenerator.gen();
		rarity_index = randint(0,3)
		self.rarity = self.creature_rarity[rarity_index]
		self.kind = random.choice(self.creature_kind)

		# A made-up equation to evaluate the max cost, based on the rarity, will probably be replace.
		# Mytic rare should be at around 15 and common at 3 i don't know if these value are remotly accurate.
		max_cost = (4*(rarity_index+1))-1;
		self.total_cost = randint(1,15) 
		self.power = randint(round(total_cost/2),total_cost)
		self.taughness = randint(round(total_cost/2),total_cost)
		self.type_line = str(self.supertype+" ─ "+self.Name)

	def rarity():
		

class Land()
		
	#> (for now all value will be selected at random just for play testing)
	color = ""
	name = ""
	tapped = False;
	supertypes = ["Basic Land","Land","Dual land","Legendary Land"]
	colors=["none","white","blue","black","red","green"]
	land_types=["Wastes","Plains","Island","Swamp","Mountain","Forest"]
	supertype = supertypes[0]
	card_type = ""
	rarity = ""
	typeline = ""

	# For a manual external way of changing the color of a mana.
	def change_color(color):
		self.color = color

	# A temporary way to gen the cards (Might be moved and changed latter.)
	def gen_land():
		if supertype == "Basic Land":
			# Select mana color
			#> (the __none__ color is for colorless mana.)

			## Local variable
			color_id = randint(0,5)

			## Global Land variable
			self.name = self.land_types[color_id]
			self.color = self.colors[color_id]

			# [Type_line](https://mtg.fandom.com/wiki/Type_line)
			self.type_line = str(self.supertype+" ─ "+self.Name)

		#> (let's just start with basic land for now)
		"""
		elif supertype == "Dual land":
			# Select mana color

			## Local variable
			color_id[0] = randint(0,5)
			# Ensure that both color are id are different.
			color_id[1] = color_id[0]
			while color_id[1] == color_id[0]:
				color_id[1] = randint(0,5)

			## Global Land variable
			self.name = namegenerator.gen();
			self.color = self.colors[0]

			#[Type_line](https://mtg.fandom.com/wiki/Type_line)
			self.type_line = str(self.supertype+" ─ "+self.Name)
		"""







