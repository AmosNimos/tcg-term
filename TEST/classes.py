## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary

from arrays import creature_kinds
import random
## Cards class
class Creature():
	name = creature_kinds[random.randint(0,len(creature_kinds))] + " of the " + creature_kinds[random.randint(0,len(creature_kinds))]
	symbol = "#"
	supertype = "Creature"
	tapped = False;
	kind = creature_kinds[random.randint(0,len(creature_kinds))]; # Human, Dinosaur Avatar, Vampire...
	power = 1;
	taughness = 1;
	cost = [1,0,0,0,0,0];
	type_line = supertype+" ─ "+name
	rarity = "common"

class Land():
		color = "none"
		name = "Wastes"
		supertype = "Basic"
		symbol = "%"

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
		for x in range(creature_count):
			self.deck.append(Creature())
		random.shuffle(self.deck)

"""
class AI:
	def __init__(self, name, self_id, deck, health, hand_size):	
"""
