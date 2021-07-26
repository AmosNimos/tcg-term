from random import choice

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

class Land()
		
		color = ""
		name = ""
		supertype = "Basic"
		rarity

		def change_color(color):
			self.color = color

		def gen_color():
			# the __none__ color is for colorless mana.

			#Select the mana color
			color_id = randint(0,5)
			colors=["none","white","blue","black","red","green"]
			names=["Wastes","Plains","Island","Swamp","Mountain","Forest"]

			self.Name = names[color_id]
			self.color = colors[color_id]






