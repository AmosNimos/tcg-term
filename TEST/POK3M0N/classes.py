## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary

# Display field function: i should add all the print together in a single string and return them instead of printing them.
import random
import sys

# Energy_colors = ["⚪️","🟣", "🔵", "⚫️", "🔴", "🟢", "🟠", "🟤", "🟡"];
# Trainor/Item/Other = [  ]
# ["⬜️","🟪","🟦","⬛️","🟥","🟩","🟧","🟫","🟨"]


## Cards class
class Pokemon():
	#Pokemon_kinds=["a","b","c"];
	kind = "";
	name = "";
	symbol = "🟧";
	color_id = 0
	symbol_char = "%"
	supertype = "Pokemon";
	HP = 1;
	taughness = 1;
	type_line = supertype+" ─ "+name;
	rarity = "common";
	energy = [0,0,0,0,0,0,0,0,0]
	
	def __init__(self):
	
		#Pokemon name generator
		def gen_name():
			Vowels = ["a","e","i","o","u"];
			Consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
			temp_name = ""
			name_size = random.randint(0,11)
			x = random.randint(0,1)
			for index in range(name_size):
				if x == 0:
					temp_name+=str(random.choice(Vowels))
					x = random.randint(0,1)
				else:
					temp_name+=str(random.choice(Consonants))
					x=0
			return temp_name

		random.Random();
		
		multi_color = False;
		
		if multi_color == True:
			self.cost = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
		else:
			color_id = random.randint(0,5)
			temp_cost = [0,0,0,0,0,0]
			temp_cost[color_id] = random.randint(1,3)
			self.cost = temp_cost
		
		# Initialise card symbol >>
		Pokemons_symbols = ["⬜️","🟪","🟦","⬛️","🟥","🟩","🟧","🟫","🟨"];
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
			self.symbol = Pokemons_symbols[0];
		else:
			self.symbol = Pokemons_symbols[self.cost.index(max(self.cost))]
	
	def tap(self):
		self.tapped=True;
		self.symbol="🔳"
		
	# So far you can only use waiste card to summon waise Pokemons... this need to be fix some how...
	# But first let's just make this shit work as, is...
	def summon(self,player):
		summon=True;
		payed_cost = [0,0,0,0,0,0]
		
		
		for color_index in range(len(self.cost)):
			untapped_Energy = 0;
			
			# [NOTE!]
			# Do i really need a separate tapped card array?
			
			#Count untapped Energy
			for Energy in range(len(player.Energy_zone[color_index])):
				if player.Energy_zone[color_index][Energy].tapped == False:
					untapped_Energy += 1;
				
			# Count total cost
			if self.cost[color_index]>len(player.Energy_zone[color_index]):
				summon=False
		
		# If their is enaugh Energy of the same color on the field
		if summon == True:
			for color_index in range(len(self.cost)):
				for Energy in range(len(player.Energy_zone[color_index])):
					#Tap the required Energy
					if payed_cost[color_index] < self.cost[color_index]:
						player.Energy_zone[color_index][Energy].tap(player);
						if self.cost[color_index] > payed_cost[color_index]:
							payed_cost[color_index] += 1;	
					
					
			player.bench_zone.append(self);
			player.hand.remove(self)
			player.console_text = "Summoning " + str(player.hand[player.cursor_x].name)	
		else:
			player.console_text = "Insufficient Energy to summon " + str(player.hand[player.cursor_x].name)
				
		# 0- count untap Energy on the Energy_zone
		# 1- check for the card cost
		# 2- tap Energy
		# 3- remove it self from the hand array
		# 4- add it self to the field
	def info(self):
		card_info += color_name[self.color_id] + color_symbol[self.color_id] + "\n"
		card_info = "Name:"+ str(self.name) + "\n" 
		card_info += "HP:[" + str(self.HP) + "]\n"
		card_info += "Rarity:" + str(self.rarity) + "\n"
		
		# When the card is on the field the effect must be interactive, some how.
		# Maybe consider effect like card zone, like object in an array maybe?
		# So we store the effect object in an array variable in the pokemon object... ?
		card_info += "Effect: [...]\n"
		return card_info

class Energy():
	color = "none";
	name = "Wastes";
	color_id = 0;
	supertype = "Basic";
	symbol = "🟪";
	symbol_char = "$"
	
	def __init__(self,*args):
	
		random.Random()
		#Manually select color
		if len(args)>0:
			color_id = args[0];
		else:
			color_id = random.randint(0,5)
		Energy_colors = ["🟣", "⚪️", "🔵", "⚫️", "🔴", "🟢"];
		colors=["none","white","blue","black","red","green"]
		names=["Wastes","Plains","IsEnergy","Swamp","Mountain","Forest"]
		self.name = names[color_id]
		self.color = colors[color_id]
		self.symbol = Energy_colors[color_id]
		self.color_id = color_id
		
	def info(self):
		card_info = "Name:"+ str(self.name) + "\n"
		card_info += self.supertype + "\n"
		return card_info
		
	def change_color(color):
		self.color = color

	def remove(self,player):
		player.Energy_zone[self.color_id].remove(self);
		
	def tap(self,player):
		self.tapped=True;
		self.symbol="🔳"
		
		# [NOTE!]
		# The "tapped_Energy" array could simply be a Integer variable and represent tapped card with a symbol for x
		# Side effect would be not being able to preview the content of the tap cards
		
		player.tapped_Energy.append(self);
		
	#def gen_color(self):
		# the __none__ color is for colorless mana.
		#Select the mana color

	
	def summon(self,player):
		# add this Energy to the Energy_zone respective color index 
		player.Energy_zone[self.color_id].append(self);
		player.hand.remove(self)

# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	
	# Strings 
	console_text ="";
	
	# Boolean
	game_over = False;
	
	#Array 1D
	collection = [];
	hand = [];
	bench_zone = [];
	battle_zone = None;
	graveyard = [];
	deck=[]; 
	
	# Int
	coins = 0;
	cursor_x = 0;
	cursor_y = 2;
	energy_use = 0; # How meny energy can the player still use this turn. (normally 1 per turn)
	
	# None/Empty
	selection = None
	
	def __init__(self, name, health):
		self.name = "Bob Smith",
		self.health = health,
		
	def shuffle_deck():
		random.shuffle(self.deck)
		
	def select():
		return None;
		# This function make the player pick a card from the field and return it.
		
	def draw(self,*args):
		# This function draw X card from the deck.
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
				
	def discard(self,*args):
		# If an argument is given it will use it as the draw amouth, 
		# otherwise it will default to 1.
		if len(args)>0:
			amounth = args[0]
		else:
			amounth = 1 
		self.console_text = "discard " + str(amounth) + " card."
		for x in range(amounth):
			player.graveyard[self.selection].append(self);
			player.hand.remove(self.selection)
			
	def turn():
		
		# Draw phase
		draw()
		#Check hand size limit. 
		if len(self.hand)>self.card_limit:
			discard(self.hand-self.card_limit);
		
	def gen_deck(self):
		# This is just a temporary solution.
		Energy_count = 30;
		Pokemon_count = 30;
		
		for x in range(Energy_count):
			self.deck.append(Energy())
		for x in range(Pokemon_count):
		#[random.randint(0,10),0,0,0,0]
			card = Pokemon()
			self.deck.append(card)
		random.shuffle(self.deck)
		
		
	def debug(self):
		# Print Console
		print("-[Console]--------------------")
		print(self.console_text)	
		# Debug: Cursor location
		print("Cursor")
		print("y:"+str(self.cursor_y)+" x:"+str(self.cursor_x))
		
		# Debug: Energy
		print("Energy")
		print(self.Energy_zone)
		print("Tapped Energy")
		print(self.tapped_Energy)
		
		
	def display_field(self):
		# String
		cursor_symbol="🔍";
		bench_zone = "";
		battle_zone = "";
		hand = "";
		card_info="";
		
		# Int 
		# (Zone Index)
		lowest_zone=0
		graveyard_y=0;
		deck_y=1;
		hand_y=2;
		bench_y=3;
		battle_y=4;
		highest_zone = 3
		

		# Wrap cursor on the y axis
		if self.cursor_y > highest_zone:
			self.cursor_y = lowest_zone;
		if self.cursor_y < lowest_zone:
			self.cursor_y = highest_zone;
			
		# battle_zone ⬇️
		if self.battle_zone!=None:
			if self.cursor_y == battle_y:
				# Wrap the cursor on the x axis
				self.cursor_x=0;
				battle_zone="";
				battle_zone = cursor_symbol;
				card_info = str(self.battle_zone[card].info());
			else:
				battle_zone = str(self.battle_zone.symbol)
			print(bench_zone)
			
		# bench_zone ⬇️
		if len(self.bench_zone)>0:
			if self.cursor_y == bench_y:
				# Wrap the cursor on the x axis
				if self.cursor_x>len(self.bench_zone)-1:
					self.cursor_x=0;
				if self.cursor_x<0:
					self.cursor_x=len(self.bench_zone)-1;
			bench_zone= ""
			for card in range(len(self.bench_zone)):
				if self.cursor_x == card:
					bench_zone += cursor_symbol;
					card_info = str(self.bench_zone[card].info());
				else:
					bench_zone += str(self.bench_zone[card].symbol)
			print(bench_zone)
			
		# hand_zone ⬇️
		if len(self.hand)>0:
			# Wrap the cursor on the x axis
			if self.cursor_y == hand_y:
				if self.cursor_x>len(self.hand)-1:
					self.cursor_x=0;
				if self.cursor_x<0:
					self.cursor_x=len(self.hand)-1;
			for card in range(len(self.hand)):
				if self.cursor_y == hand_y and len(self.hand)<1:
					self.cursor_y=deck_y;
				if self.cursor_x == card and self.cursor_y == hand_y:
					hand += cursor_symbol; 
					card_info = str(self.hand[card].info());	
				else:
					hand += str(self.hand[card].symbol);
			print(hand+"["+str(len(self.hand))+"]");
			
		# deck_zone ⬇️
		if len(self.deck)<=0:
			self.game_over=True;
		else:
			if self.cursor_y == deck_y:
				self.cursor_x = 0;
				print(cursor_symbol+"["+str(len(self.deck))+"]")
			else:
				print("⬜["+str(len(self.deck))+"]")
				
		# graves_zone ⬇️
		if self.cursor_y == graveyard_y:
			self.cursor_x = 0;
			print(cursor_symbol+"["+str(len(self.graveyard))+"]")
		else:
			print("💀["+str(len(self.graveyard))+"]")
			
		# Print Info
		print("-[Info]----------------------")
		print(card_info)
		
		self.debug()
					

			
			
class AI:
	#side_board = []
	collection = [];
	coin = 0;
	hand = [];
	Energy_zone = [];
	bench_zone = [];
	permanents_zone = []; # for artefacts, enchantments, plainwalkers?, non-Pokemon.
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
		Energy_count = 30;
		Pokemon_count = 30;
		
		for x in range(Energy_count):
			self.deck.append(Energy())
		for x in range(Pokemon_count):
			self.deck.append(Energy())
		random.shuffle(self.deck)
