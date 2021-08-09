## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary

from arrays import creature_kinds
import random
## Cards class
class Creature():
	#creature_kinds=["a","b","c"];
	kind = "";
	name = "";
	symbol = "#";
	supertype = "Creature";
	power = 1;
	taughness = 1;
	cost = [1,0,0,0,0,0];
	type_line = supertype+" ─ "+name;
	rarity = "common";
	tapped = False;
	
	def __init__(self):
		self.kind = creature_kinds[random.randint(0,len(creature_kinds)-1)]; # Human, Dinosaur Avatar, Vampire...
		self.name = creature_kinds[random.randint(0,len(creature_kinds)-1)] + " of the " + creature_kinds[random.randint(0,len(creature_kinds)-1)]	

	def summon(self,lands_zone):

		
		# 0- count untap land on the land_zone
		available_land_count = [0,0,0,0,0]
		for x in len(lands_zone):
			if lands_zone[x].tapped == False:
				available_land_count[lands_zone[x].color_index]+=1;
			
		# 1- check for the card cost
		"""
		for x in len(cost):
			if cost[x] < available_land_count[x]:
				for x in cost[x]:
		"""
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
		# add this land to the lands_zone color index 
		player.lands_zone[self.color_id].append(self);
		# remove self from hand array. not sure this methode will work...
		player.hand.remove(self)

# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	lands_zone = [[],[],[],[],[],[]]; # lands are divided by color in this 2d array. so you can easily know how meny of each color their is with len(lands_zone[index])
	creatures_zone = [];
	permanents_zone = []; # for artefacts, enchantments, plainwalkers?, non-creature.
	graveyard = [];
	deck=[];
	cursor_x = 0;
	cursor_y = 1;
	
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
	cursor_y = 1;
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
