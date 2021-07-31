## Don't worry every part of the code you don't like are just tamporary test

from arrays import creature_kinds
import random
## Cards class
class Creature():
	def __init__(self, power, taughness, cost, card_kind):
		self.power = power;
		self.taughness = taughness;
		self.kind = card_kind; # Human, Dinosaur Avatar, Vampire...
		self.cost = cost;
		self.name = creature_kinds[random.randint(0,len(creature_kinds))] + " of the " + creature_kinds[random.randint(0,len(creature_kinds))]
		self.taped = False;

class Land():
		color = "none"
		name = "Wastes"
		supertype = "Basic"

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

# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	mana_zone = [];
	field_zone = []; 
	graveyard = [];
	deck=[];

	def __init__(self, name, health):
		self.name = "Bob Smith",
		self.health = health,
		
	def gen_deck(self):
		# This is just a temporary solution.
		land_count = 30;
		creature_count = 30;
		
		for x in range(land_count):
			self.deck.append(Land())
		creature_cost = [1,0,0,0,0,0];
		for x in range(creature_count):
			self.deck.append(Creature(1,1,creature_cost,creature_kinds[random.randint(0,len(creature_kinds))]))
		random.shuffle(self.deck)

"""
class AI:
	def __init__(self, name, self_id, deck, health, hand_size):	
"""
