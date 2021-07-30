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
			colors=["none","basic","white","blue","red","green"]
			names=["Wastes","Plains","Island","Swamp","Mountain","Forest"]

			self.Name = names[color_id]
			self.color = colors[color_id]

# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	collection = [],
	coin = 0,
	hand = [],
	mana_zone = [],
	field_zone = [], 
	graveyard = [],
	def __init__(self, name, self_id, deck, health, hand_size):
		self.name = "Bob Smith",
		self.self_id = self_id,
		self.deck = deck,
		self.hand = hand,
		self.health = health,
		
class AI:
	def __init__(self, name, self_id, deck, health, hand_size):
		
class AI:
	def __init__(self, name, self_id, deck, health, hand_size):
		
