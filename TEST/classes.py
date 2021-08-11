## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary

from arrays import creature_kinds
import random
import sys

## Cards class
class Creature():
	#creature_kinds=["a","b","c"];
	kind = "";
	name = "";
	symbol = "#";
	cost = [1,0,0,0,0];
	supertype = "Creature";
	power = 1;
	taughness = 1;
	type_line = supertype+" ─ "+name;
	rarity = "common";
	tapped = False;
	
	def __init__(self):
		self.kind = creature_kinds[random.randint(0,len(creature_kinds)-1)]; # Human, Dinosaur Avatar, Vampire...
		self.name = creature_kinds[random.randint(0,len(creature_kinds)-1)] + " of the " + creature_kinds[random.randint(0,len(creature_kinds)-1)]	


	def summon(self,player):
		# If their is eneugh land to cover the card cost tapp them
		payed_cost = [0,0,0,0,0];
		for color_index in range(len(self.cost)):
			if len(player.lands_zone[color_index]) >= self.cost[color_index]:
				for land in range(len(player.lands_zone[color_index])):
					if player.lands_zone[color_index][land].tapped == False:
						player.lands_zone[color_index][land].tap();
						if self.cost[color_index] > payed_cost[color_index]:
							payed_cost[color_index] +=1;		
			else:
				return 0
		if payed_cost == self.cost:
			player.creatures_zone.append(self);
			player.hand.remove(self)	
		else:
			print("insufficient lands")
			print(payed_cost)
			print("<")
			print(self.cost)
			input()
				
		# 0- count untap land on the land_zone
		# 1- check for the card cost
		# 2- tap land
		# 3- remove it self from the hand array
		# 4- add it self to the field

class Land():
	color = "none";
	name = "Wastes";
	color_id = 0;
	supertype = "Basic";
	symbol = "%";
	tapped = False;

	def change_color(color):
		self.color = color

	def tap(self):
		self.tapped=True;
		self.symbol="x"
		
		
		
	def gen_color():
		# the __none__ color is for colorless mana.
		#Select the mana color
		color_id = randint(0,5)
		colors=["none","white","blue","black","red","green"]
		names=["Wastes","Plains","Island","Swamp","Mountain","Forest"]
		self.Name = names[color_id]
		self.color = colors[color_id]
		self.color_id = color_id
	
	def summon(self,player):
		# add this land to the lands_zone respective color index 
		player.lands_zone[self.color_id].append(self);
		player.hand.remove(self)

# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	# the last array in the lands_zone array is for tapped land.
	lands_zone = [[],[],[],[],[],[]]; # lands are divided by color in this 2d array. so you can easily know how meny of each color their is with len(lands_zone[index])
	tapped_lands = [];
	creatures_zone = [];
	permanents_zone = []; # for artefacts, enchantments, plainwalkers?, non-creature.
	graveyard = [];
	deck=[];
	cursor_x = 0;
	cursor_y = 2;
	
	def __init__(self, name, health):
		self.name = "Bob Smith",
		self.health = health,
		
	def shuffle_deck():
		random.shuffle(self.deck)
		
	def draw(self,amounth):
		for x in range(amounth):
			draw = self.deck[-1]
			self.deck.pop()
			self.hand.append(draw)
		
	def gen_deck(self):
		# This is just a temporary solution.
		land_count = 30;
		creature_count = 30;
		
		for x in range(land_count):
			self.deck.append(Land())
		for x in range(creature_count):
			self.deck.append(Creature())
		random.shuffle(self.deck)


class AI:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	lands_zone = [];
	creatures_zone = [];
	permanents_zone = []; # for artefacts, enchantments, plainwalkers?, non-creature.
	graveyard = [];
	deck=[];
	cursor_x = 0;
	cursor_y = 2;
	card_back="?"
	
	def __init__(self, name, health):
		self.name = "BOT",
		self.health = health,
		
	def shuffle_deck():
		random.shuffle(self.deck)
		
	def draw(self,amounth):
		for x in range(amounth):
			draw = self.deck[-1]
			self.deck.pop()
			self.hand.append(draw)
		
	def gen_deck(self):
		# This is just a temporary solution.
		land_count = 30;
		creature_count = 30;
		
		for x in range(land_count):
			self.deck.append(Land())
		for x in range(creature_count):
			self.deck.append(Creature())
		random.shuffle(self.deck)
