## Don't worry every part of the code you don't like are just tamporary test, all value hard coded are temporary

# Display field function: i should add all the print together in a single string and return them instead of printing them.
import random
import sys

# Energy_colors = ["⚪️","🟣", "🔵", "⚫️", "🔴", "🟢", "🟠", "🟤", "🟡"];
# Trainor/Item/Other = [  ]
# ["⬜️","🟪","🟦","⬛️","🟥","🟩","🟧","🟫","🟨"]

class move():
	def cost_to_string(self, cost):
		color_list = ["⚪️","🟣", "🔵", "⚫️", "🔴", "🟢", "🟠", "🟤", "🟡"];
		cost_string=""
		for x in range(len(cost)):
			cost_string += str(color_list[x])*cost[x]
		return cost_string
	# This class define one move the pokemon can use and it's effect. 
	def __init__(self, pokemon, index):
		random.Random();
		temp_cost = [0,0,0,0,0,0,0,0,0]
		temp_total_cost=0;
		if pokemon.color_id != 0:
			temp_cost[0] = random.randint(1-index,4-index)
			temp_total_cost = temp_cost[0]
		temp_cost[pokemon.color_id] = random.randint(1+index,5-temp_cost[0])
		temp_total_cost += temp_cost[pokemon.color_id]
		name_list=["Punch","Kick","Bite","Tackle","Push","Cut"]
		self.effect_string = ""
		self.name = random.choice(name_list)
		self.cost = temp_cost
		self.total_cost = temp_total_cost;
		self.damage = temp_total_cost*(10+(index*5))*pokemon.stage;
		self.cost_string = self.cost_to_string(temp_cost)
		
	
			
	
		
		
## Cards class
class pokemon():
	#pokemon_kinds=["a","b","c"];
	kind = "";
	name = "";
	symbol = "⬜️";
	color_id = 0
	symbol_char = "%"
	stage = 0 
	supertype = "Basic";
	supertype_list = ["Basic","First","Final"]
	HP = 1;
	taughness = 1;
	type_line = supertype+" ─ "+name;
	rarity = 0;
	rarity_list = ["Common","Uncommon","Rare","Holo Rare", "Reverse Holo", "Full Art", "Secret Rare", "Rainbow Rare", "Promo"]
	energy = [0,0,0,0,0,0,0,0,0]
	temp_cost = [0,0,0,0,0,0,0,0,0];
	temp_total_cost=0;
	
	def __init__(self,stage,evo_from,color_id,rarity):
		
		random.Random();
			
		self.name=self.gen_name()
		if rarity == None:
			self.rarity = random.randint(0,3);
		else:
			self.rarity = rarity;
		# Initialise card symbol >>
		symbol_list = ["⬜️","🟪","🟦","⬛️","🟥","🟩","🟧","🟫","🟨"];
		if color_id == None:
			self.color_id = random.randint(0,len(symbol_list)-1)
		else: 
			self.color_id = color_id
		self.symbol=symbol_list[self.color_id];
		# Resistance and Weakness add or substract 20 damage to an attack.
		self.resistance_type = random.randint(0,len(symbol_list)-1)
		self.weakness_type = random.randint(0,len(symbol_list)-1)
		self.symbol = symbol_list[self.color_id]
		self.stage = stage
		if stage>1:
			self.evo_from = evo_from;
		else:
			self.evo_from = None;
		
		self.supertype = self.supertype_list[self.stage-1]
		self.gen_move()
		
		# Set move_list
		

		
	def gen_move(self):
		
		## First move
		self.move_list=[move(self, 0),move(self, 1)]
		print(self.move_list)
			
	#pokemon name generator
	def gen_name(self):
		Vowels = ["a","e","i","o","u"];
		Consonants = ['b', 'c', 'ch', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
		temp_name = ""
		name_size = random.randint(2,6)
		x = random.randint(0,1)
		for index in range(name_size):
			if x == 0:
				temp_name+=str(random.choice(Vowels))
				x = random.randint(0,1)
			else:
				temp_name+=str(random.choice(Consonants))
				x=0
			# Make the first letter Uppercase
			temp_name = temp_name[0].upper() + temp_name[1:]
		return temp_name
			
	def info(self):
		#card_info += color_name[self.color_id] + color_symbol[self.color_id] + "\n"
		card_info = "";
		card_info += "Stage: "+str(self.supertype)+"\n";
		if self.evo_from != None:
			card_info += "Evolve from "+str(evo_from);
		card_info += "Name: "+str(self.name) + "\n" 
		card_info +=	"type: "+self.symbol+ "\n"
		card_info += "HP:[" + str(self.HP) + "]\n"
		card_info += "Rarity:" + str(self.rarity) + "\n"
		
		# When the card is on the field the effect must be interactive, some how.
		# Maybe consider effect like card zone, like object in an array maybe?
		# So we store the effect object in an array variable in the pokemon object... ?
		
		# Moves
		card_info += "Moves:\n  ["
		card_info += str(self.move_list[0].cost_string)+"] "+str(self.move_list[0].name)+" "+str(self.move_list[0].damage)+"\n  ["
		card_info += str(self.move_list[0].effect_string)
		card_info += str(self.move_list[1].cost_string)+"] "+str(self.move_list[1].name)+" "+str(self.move_list[1].damage)+"\n"		
		card_info += str(self.move_list[1].effect_string)
				
		return card_info

class Energy():
	color = "none";
	name = "Wastes";
	color_id = 0;
	supertype = "Energy";
	symbol = "🟪";
	symbol_char = "$"
	
	def __init__(self,*args):
	
		random.Random()
		#Manually select color
		if len(args)>0:
			color_id = args[0];
		else:
			color_id = random.randint(0,5)
		Energy_colors = ["⚪️","🟢", "🔴", "🔵", "🟡", "🟣", "🟠", "⚫️", "🟤"];
		names=["colorless","Grass","Fire","Water","Lightning","Psychic","Fighting","Darkness","Metal","Fairy"]
		colors=["none","white","blue","black","red","green"]
		self.name = names[color_id]
		self.color = colors[color_id]
		self.symbol = Energy_colors[color_id]
		self.color_id = color_id
		
	def info(self):
		card_info = ""
		card_info += self.supertype + "\n"
		card_info += "Name:"+ str(self.name) + "\n"
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
	## Phrase
	summon_phrase = " let's go!"
	
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
	## Zones
	lowest_y=0
	graveyard_y=0;
	deck_y=1;
	hand_y=2;
	bench_y=3;
	battle_y=4;
	highest_y = 4
	
	## Max
	max_bench = 5
	
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
		
		
	def summon(self,selected):
			if self.cursor_y == self.hand_y:
				#Place Pokemon from hand_zone to bench_zone
				if len(self.bench_zone) < self.max_bench:
					self.bench_zone.append(selected);
					self.hand.remove(selected)
					self.console_text = str(selected.name) + self.summon_phrase
				else:
					self.console_text = "Your bench zone is already full!"
			if self.cursor_y == self.bench_y:
				#Place Pokemon from bench_zone to battle_zone.
				if self.battle_zone==None:
					self.battle_zone=selected;
					self.bench_zone.remove(selected)
					self.console_text = str(selected.name) + self.summon_phrase
				else:
					self.console_text = str(self.battle_zone.name) + " is already in battle."
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
		pokemon_count = 30;
		
		for x in range(Energy_count):
			self.deck.append(Energy())
		for x in range(pokemon_count):
		#[random.randint(0,10),0,0,0,0]
			card = pokemon()
			self.deck.append(card)
		random.shuffle(self.deck)
		
		
	def debug(self):
		# Print Console
		print("-[Console]--------------------")
		print(self.console_text)	
		# Debug: Cursor location
		print("Cursor")
		print("y:"+str(self.cursor_y)+" x:"+str(self.cursor_x))
		
		
	def display_field(self):
		# String
		cursor_symbol="🔍";
		bench_zone = "";
		battle_zone = "";
		hand = "";
		card_info="";
		
		# Int 
		# (Zone Index)
		

		# Wrap cursor on the y axis
		if self.cursor_y > self.highest_y:
			self.cursor_y = self.lowest_y;
		if self.cursor_y < self.lowest_y:
			self.cursor_y = self.highest_y;
			
		# battle_zone ⬇️
		if self.battle_zone!=None:
			if self.cursor_y == self.battle_y:
				# Wrap the cursor on the x axis
				self.cursor_x=0;
				battle_zone="";
				battle_zone = cursor_symbol;
				card_info = str(self.battle_zone[card].info());
			else:
				battle_zone = str(self.battle_zone.symbol)
			print("["+battle_zone+"]")
		else:
			print("[  ]")
			
		# bench_zone ⬇️
		if len(self.bench_zone)>0:
			if self.cursor_y == self.bench_y:
				# Wrap the cursor on the x axis
				if self.cursor_x>len(self.bench_zone)-1:
					self.cursor_x=0;
				if self.cursor_x<0:
					self.cursor_x=len(self.bench_zone)-1;
			bench_zone= ""
			for card in range(len(self.bench_zone)):
				if self.cursor_x == card and self.cursor_y == self.bench_y:
					bench_zone += cursor_symbol;
					card_info = str(self.bench_zone[card].info());
				else:
					bench_zone += str(self.bench_zone[card].symbol)
			for empty in range(self.max_bench-len(self.bench_zone)):
					bench_zone += "  "
			print("["+bench_zone+"]")
		else:
			print("[          ]")
			
		# hand_zone ⬇️
		if len(self.hand)>0:
			# Wrap the cursor on the x axis
			if self.cursor_y == self.hand_y:
				if self.cursor_x>len(self.hand)-1:
					self.cursor_x=0;
				if self.cursor_x<0:
					self.cursor_x=len(self.hand)-1;
			for card in range(len(self.hand)):
				if self.cursor_y == self.hand_y and len(self.hand)<1:
					self.cursor_y=self.deck_y;
				if self.cursor_x == card and self.cursor_y == self.hand_y:
					hand += cursor_symbol; 
					card_info = str(self.hand[card].info());	
				else:
					hand += str(self.hand[card].symbol);
			print(hand+"["+str(len(self.hand))+"]");
			
		# deck_zone ⬇️
		if len(self.deck)<=0:
			self.game_over=True;
		else:
			if self.cursor_y == self.deck_y:
				self.cursor_x = 0;
				print(cursor_symbol+"["+str(len(self.deck))+"]")
			else:
				print("⬜["+str(len(self.deck))+"]")
				
		# graves_zone ⬇️
		if self.cursor_y == self.graveyard_y:
			self.cursor_x = 0;
			print(cursor_symbol+"["+str(len(self.graveyard))+"]")
		else:
			print("💀["+str(len(self.graveyard))+"]")
			
		# Print Info
		print("-[Info]----------------------")
		print(card_info)
		
		self.debug()
					

class menu():

	room=0;
	#⮕➤👉
	cursor_symbol="👉"; # Their should be a single cursor_symbol variable inside the player class
	max_y = 2
	battle_y = 2;
	shop_y=1;
	collection_y=0;
	min_y = 0
	def display(self,player):
		print()
		#wrap y cursor
		if player.cursor_y>self.max_y:
			player.cursor_y = self.min_y;
		elif player.cursor_y<self.min_y:
			player.cursor_y = self.max_y;
				
		if player.cursor_y == self.battle_y:
			print("   "+self.cursor_symbol+" Battle")
			#room=1;
		else:
			print("   "+"Battle")
			
		if player.cursor_y == self.shop_y:
			print("   "+self.cursor_symbol+" Shop")
		else:
			print("   "+"Shop")
			
		if player.cursor_y == self.collection_y:
			print("   "+self.cursor_symbol+" Collection")
		else:
			print("   "+"Collection")

class shop:
	def gen_booster(self):
		# This is just a temporary solution.
		pokemon_count = 10;
		booster=[]
		for x in range(pokemon_count):
			# gen Basic stage
			card = pokemon(1,None,None,None)
			basic_stage = card.name
			basic_color_id = card.color_id
			basic_rarity = card.rarity
			booster.append(card)
			# gen first stage of evolution
			card = pokemon(2,basic_stage,basic_color_id,basic_rarity)
			first_stage = card.name
			booster.append(card)
			# gen first stage of evolution
			card = pokemon(3,first_stage,basic_color_id,basic_rarity)
			booster.append(card)
			
		random.shuffle(self.booster)
		return booster		
		
		
## All pokemon effect go here
"""
class critical_hit():
	def __init__(self, value):
		self.value = value
		self.description = "Flip a coin, if head this attack does +"+str(value)+" damage."
		
	def flip_coin():
	
	def effect(self):
		if flip_coin == True:
			return self.value
			
"""
