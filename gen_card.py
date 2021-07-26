from random import choice

## 

## Cards class
class Creature:
	def __init__(self, power, taughness, cost, card_kind):
		self.power = power;
		self.taughness = taughness;
		self.kind = card_kind; # Human, Dinosaur Avatar, Vampire...
		self.cost = cost;
		self.total_cost = total_cost;
		self.name = namegenerator.gen();
		self.taped = False;
		self.rarity = 

	def rarity():
		creature_rarity = ["common","uncomon","rare","mythic rare"]

class Land()
		
		#> (for now all value will be selected at random just for play testing)
		color = ""
		name = ""
		supertypes = ["Basic Land","Land","Dual land","Legendary Land"]
		colors=["none","white","blue","black","red","green"]
		names=["Wastes","Plains","Island","Swamp","Mountain","Forest"]
		supertype = supertypes[0]
		card_type = ""
		rarity = ""
		typeline = ""

		def change_color(color):
			self.color = color

		def gen_land():
			if supertype == "Basic Land":
				# Select mana color
				#> (the __none__ color is for colorless mana.)

				## Local variable
				color_id = randint(0,5)

				## Global Land variable
				self.name = self.names[color_id]
				self.color = self.colors[color_id]

				#[Type_line](https://mtg.fandom.com/wiki/Type_line)
				self.type_line = str(self.supertype+" ─ "+self.Name)

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











