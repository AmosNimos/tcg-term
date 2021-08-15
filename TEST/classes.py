## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary

from arrays import creature_kinds
import random
import sys

# lands_colors = ["🟣", "⚪️", "🔵", "⚫️", "🔴", "🟢"];
# Permanent = [🟠 🟡 🟤]
# Creature 


## Cards class
class Creature():
	#creature_kinds=["a","b","c"];
	kind = "";
	name = "";
	symbol = "🟧";
	symbol_char = "%"
	supertype = "Creature";
	power = 1;
	taughness = 1;
	type_line = supertype+" ─ "+name;
	rarity = "common";
	tapped = False;
		
	def __init__(self):
		random.Random()
		self.cost = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
		self.kind = creature_kinds[random.randint(0,len(creature_kinds)-1)]; # Human, Dinosaur Avatar, Vampire...
		self.name = creature_kinds[random.randint(0,len(creature_kinds)-1)] + " of the " + creature_kinds[random.randint(0,len(creature_kinds)-1)]	
		
		# Initialise card symbol >>
		creatures_symbols = ["🟪","⬜️","🟦","⬛️","🟥","🟩"]
		# Check for multi color card
		costs = []
		for x in self.cost:
			if x != 0:
				costs.append(x)
		no_duplicates = set(costs)
		contains_duplicates = len(no_duplicates) != len(costs)
		# Find the largest cost in the cost array then get it's index then use it as this card color.
		if contains_duplicates == True:
			# set the card color to colorless. 
			self.symbol = creatures_symbols[0];
		else:
			self.symbol = creatures_symbols[self.cost.index(max(self.cost))]
	
	def tap(self):
		self.tapped=True;
		self.symbol="🔳"
		
	# So far you can only use waiste card to summon waise creatures... this need to be fix some how...
	# But first let's just make this shit work as, is...
	def summon(self,player):
		summon=True;
		payed_cost = [0,0,0,0,0,0]
		for color_index in range(len(self.cost)):
			# Count total cost
			if self.cost[color_index]>len(player.lands_zone[color_index]):
				summon=False
		
		# If their is enaugh land of the same color on the field
		if summon == True:
			for color_index in range(len(self.cost)):
				for land in range(len(player.lands_zone[color_index])):
					#Tap the required lands
					if payed_cost[color_index] < self.cost[color_index]:
						player.lands_zone[color_index][land].tap(player);
						if self.cost[color_index] > payed_cost[color_index]:
							payed_cost[color_index] +=1;	
			player.creatures_zone.append(self);
			player.hand.remove(self)
			player.console_text = "Summoning " + str(player.hand[player.cursor_x].name)	
		else:
			player.console_text = "Insufficient lands to summon " + str(player.hand[player.cursor_x].name)
			

				
		# 0- count untap land on the land_zone
		# 1- check for the card cost
		# 2- tap land
		# 3- remove it self from the hand array
		# 4- add it self to the field
	def info(self):
		card_info = "Name:"+ str(self.name) + "\n" 
		card_info += "Cost:"+ str(self.cost) + "\n"
		card_info += self.supertype + "\n"
		card_info += "Rarity:" + str(self.rarity) + "\n"
		card_info += "Effect: [...]\n"
		card_info += "Power:[" + str(self.power) + "]\n"
		card_info += "Power:[" + str(self.taughness) + "]\n"
		return card_info

class Land():
	color = "none";
	name = "Wastes";
	color_id = 0;
	supertype = "Basic";
	symbol = "🟪";
	symbol_char = "$"
	tapped = False;
	
	def __init__(self,*args):
		random.Random()
		#Manually select color
		if len(args)>0:
			color_id = args[0];
		else:
			color_id = random.randint(0,5)
		lands_colors = ["🟣", "⚪️", "🔵", "⚫️", "🔴", "🟢"];
		colors=["none","white","blue","black","red","green"]
		names=["Wastes","Plains","Island","Swamp","Mountain","Forest"]
		self.name = names[color_id]
		self.color = colors[color_id]
		self.symbol = lands_colors[color_id]
		self.color_id = color_id
		
	def info(self):
		card_info = "Name:"+ str(self.name) + "\n"
		card_info += self.supertype + "\n"
		return card_info
	def change_color(color):
		self.color = color

	def tap(self,player):
		self.tapped=True;
		self.symbol="🔳"
		player.tapped_lands.append(self);
		player.lands_zone[self.color_id].remove(self)
		
	#def gen_color(self):
		# the __none__ color is for colorless mana.
		#Select the mana color

	
	def summon(self,player):
		# add this land to the lands_zone respective color index 
		player.lands_zone[self.color_id].append(self);
		player.hand.remove(self)

# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	game_over = False;
	collection = [];
	coin = 0;
	hand = [];
	# the last array in the lands_zone array is for tapped land.
	lands_zone = [[],[],[],[],[],[]]; # lands are divided by color in this 2d array. so you can easily know how meny of each color their is with len(lands_zone[index])
	tapped_lands = [];
	creatures_zone = [];
	tapped_creatures = [];
	permanents_zone = []; # for artefacts, enchantments, plainwalkers?, non-creature.
	graveyard = [];
	deck=[];
	cursor_x = 0;
	cursor_y = 2;
	console_text ="";
	
	def __init__(self, name, health):
		self.name = "Bob Smith",
		self.health = health,
		
	def shuffle_deck():
		random.shuffle(self.deck)
		
	def draw(self,*args):
		# If an argument is given it will use it as the draw amouth, 
		# otherwise it will default to 1.
		if self.game_over == False:
		
			if len(args)>0:
				amounth = args[0]
			else:
				amounth = 1 
			self.console_text = "Draw " + str(amounth) + " card."
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
		#[random.randint(0,10),0,0,0,0]
			card = Creature()
			self.deck.append(card)
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
			self.deck.append(Land())
		random.shuffle(self.deck)
