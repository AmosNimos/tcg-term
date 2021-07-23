# Imports
from random import randint
from random import shuffle
from random import sample
import os

## External dependency
from termcolor import colored, cprint
import namegenerator
from curtsies import Input
import pyttsx3

# Vars
## Rules Variables
deck_size = 60;
initial_health = 20;

# Game Variables 
players = []; # A list containing all player object.
player_turn = 0; # Why is this an array? I forgot.

# Cursor selection	
#class selection: 
#	def __init__(self, x, y, over, selected):

# Class
## Cards class
### Creature, Land and other card type card class
### (Color cost could be stored in an array with five index of integer representing the color cost, and an extra index for the color less cost.)
class Card:
	def __init__(self, self_id, power, taughness, cost, total_cost, color, card_type, card_kind):
		self.self_id = self_id;
		self.power = power;
		self.taughness = taughness;
		self.type = card_type; # Sorcery, Land, Enchantment, Creature...
		self.kind = card_kind; # Human, Dinosaur Avatar, Vampire...
		self.cost = cost;
		self.total_cost = total_cost;
		self.name = namegenerator.gen();
		self.taped = False;
		
		# Make a function to calculate what color the creature is based on the mana cost array.
		# IF, their is a need for it in the game otherwise just ignore it.

		# I need this variable for mana/plane.
		self.color = color;
			
		
# Player 
## (Don't forget to add an extra deck)	
## (You can use 2D array to stack card in the same place.)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	def __init__(self, name, self_id, deck, health, hand, mana_zone, field_zone, graveyard, Playable):
		self.name = name
		self.self_id = self_id
		self.deck = deck 
		self.hand = hand
		self.health = health
		self.mana_zone = mana_zone
		self.field_zone = field_zone
		self.graveyard = graveyard
		
	def select_card(source, player):
		# Here a card can be selected from source array by player
		## This process should be automated when playing against the machine.
		### Exception may need to be applied in a way or another, like the card type or color, or cost, or inded (position) in the source array.
		return selection
	
	# def move_card(source, selected, destination):
		# Card zone change	
		## (Basically a function to move a card from any zone, to any zone if, an effect or situation require it.)
		### zone = graveuard, hand. field, deck...
		#### Remove selected card from source (zone) array and add it to destination (zone) array.		
	
			
### Function about card generation
def Generate_cost():
	# NOTE: (This function is way too big, if you know how to simplify it and make it clearer and shorter, feel free to suggest a your change to this project.)
	
	# Color order 🚫⚪🔵⚫🔴🟢
	final_cost = [0,0,0,0,0,0]; 
	ratio = cost_ratio()
	print("card colors: "+str(ratio))
	if ratio > 0:
		max_cost = 15/ratio
	else:
		max_cost = 15
	print("max_cost_before:"+str(max_cost))
	min_cost = 1

	
	if ratio == 0:
		print("r0")
		current_cost = randint(1, round(15/randint(1,4))); 
		# making larger cost less likely 
		for x in range(current_cost):
			maximum_limit = randint(2,4);
			if randint(0,17-current_cost) == 0 and current_cost>maximum_limit:
				current_cost -= randint(1,maximum_limit);
		final_cost[0]
	else:	
		# If NOT all mana color including colorless are in the ratio, select a random value to each equal to the ratio of color.	
		# Remove the minimum cost multiplied by the amounth of color index in the array. since it will be added by default
		
		# Loop for ratio amounth of index in the final_cost array and add a random value.
		for cost_index in range(ratio):
			print("max="+str(max_cost))
			current_cost = randint(1, round(max_cost));
			# making larger cost less likely 
			# this is way overcomplicated for no reason, please help me
			for x in range(current_cost):
				maximum_limit = randint(2,4);
				if randint(0,17-current_cost) == 0 and current_cost>randint(2,4):
					current_cost -= randint(1,randint(2,4));
			max_cost -= current_cost;
			if max_cost < 1:
				max_cost = 1;
				if final_cost[cost_index-1]>1:
					final_cost[cost_index-1]=round(final_cost[cost_index-1]/2)
			final_cost[cost_index] = current_cost; 
	
		# shuffle the cost array.
		shuffle(final_cost)
		
	return final_cost

# Generate deck
def gen_creature(card_index):
	cost_limit=0

	# for each player, Loop trough for each card in the deck and generate them, and append them to deck.
	#Calculate the total mana cost of the card
	new_cost = Generate_cost();
	total_cost=0;
	for cost_index in range(len(new_cost)):
		total_cost+=new_cost[cost_index]

	print("total_cost: "+str(total_cost))
	print("color: [🚫,⚪,🔵,⚫,🔴,🟢]")
	print("cost : "+str(new_cost))
	limiters = [4,8,10,12,14,16,18,20,22,24,25,26,27,28,29,30,32]
	cost_limit = limiters[total_cost]
	print(cost_limit)
	
	# Generate 
	power = randint(0,total_cost*2+round(total_cost/2))
	taughness = randint(0,total_cost*2+round(total_cost/2))

	# Function to regulate the somme of both powerr and taughness based on the mana cost
	# like while p+t > limit, random(0,1) if 1 p-1, esle t-1
	while power + taughness > cost_limit:
		# Choose what atribute to debuff.
		if randint(0,1) == 1:
			power-=1;
		else:
			taughness-=1;
	
	# Maximum value based on the following, online reference.
	# https://www.reddit.com/r/EDH/comments/ogiko4/low_cost_high_power_creatures/
	# power + taughness limit:
	# These value and formula can be change in the limiters array if needed, to be more similar to the original game.
	# Some self adverse effect can also increase a card initial default power and taughness, to compensate.
	# From 1 mana to 5 in this array, so far no creature cost 0 mana.
	
	return Card(card_index, power, taughness, new_cost, total_cost, None, "creature", "Vampire")
	
def gen_land():
	return Card(None, None, None, "Land")	
		
# Combine all visual element layout in a single string variable and print it to the terminal to display frame.
def draw_frame(top,mid,end):		
	print(frame)
	
# Initialise the game parameter
def Game_init():
	# Generate both player decks
	temp_deck = []
	for card in range(deck_size):
		new_card = gen_creature(card)
		temp_deck.append(new_card)
	
	first_deck = temp_deck
	second_deck = temp_deck
	# Generate Players.
	#(name, self_id, deck, hand, health, mana_zone, field_zone, graveyard, Playable):
	new_player = Player("Main_player",0,first_deck,initial_health,None, None,None,None, True)
	players.append(new_player)
	new_player = Player("Ai_player",1,second_deck,initial_health,None, None,None,None, False)
	players.append(new_player)
	# Select who will start
	player_turn=randint(0,1);
	os.system('clear')
	


# This function is for creating color pack
# generate card in the card variable 
"""
def color_pack:
	while pack < pack_size: 
		if card.card_type == "land" and card.color == pack_color:
			pack.append(card)
		elif card.card_type == "creature" and cost[pack_color_index] > 0:
			pack.append(card)
			
"""

# Functions
## Return keypress input from curtsies
def get_input():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e
def rarity_ratio:
	if randint(0,1000) == 0 :
		# Value suggestion
		# Can be 6 color creature (including colorless)
		# with a max cost of 15
		return "mythic rare"
	elif randint(0,500) == 0 :
		# Can be 5 color creature (including colorless)
		# with a max cost of 12
		return "rare"
	elif randint(0,100) == 0 :
		# Can be 4 color creature (including colorless)
		# with a max cost of 10
		return "uncomon"
	else:
		# Cannot be more then 3 color creature (including colorless)
		# 9 max cost
		return "common"
	
# color Cost ratio
def cost_ratio():
	
	# The ratio is based on 1 over the x_color_ratio value.
	# If the value is equal to 0 the card will have the following X amounth of color mana cost diversity.
	# Otherwise it will try the following ratio in order 
	# if none of the value return 0 then the card will be colorless.
	
	one_color_ratio = 2
	two_color_ratio = 8
	tree_color_ratio = 25
	four_color_ratio = 50
	five_color_ratio = 75
	six_color_ratio = 100
	
	if randint(0,one_color_ratio) == 0:
		#One color attribute (excluding colorless)
		return 1
	elif randint(0,two_color_ratio) == 0:
		#Two color attribute
		return 2
	elif randint(0,tree_color_ratio) == 0:
		#Tree color attribute
		return 3
	elif randint(0,four_color_ratio) == 0:
		#four color attribute
		return 4
	elif randint(0,five_color_ratio) == 0:
		#five color attribute
		return 5
	elif randint(0,six_color_ratio) == 0:
		#six color attribute (all color atribute, including colorless)
		return 6 
	else: 
		#No color attribute
		return randint(randint(0,1),4+randint(0,2))	
		
# Take an array of card and return an array containing only the card coresponding to the argument given	
def exception(array,max_cost,min_cost,card_type,in_name,max_power,min_power,max_taughness,min_taughness):
	picked = []
	
	# Only pick cards between max_cost and min_cost. (default 0,12 for all cost)
	for x in array:
		for cost_index in range(len(x.cost)):
			if x.cost[cost_index] < max_cost and x.cost[cost_index] > min_cost:
				picked.append(x)
	
	# Replace the array with the new selection of cards.
	array = picked
	
	# Only pick cards of X type.
	if card_type != None:
		for x in array:
			if x.type == card_type:
				picked.append(x)
				
	# Replace the array with the new selection of cards.
	array = picked
	
	return array
		
# emoji idea for the card pack "📗📦🎴"
# Game ui: Main_menu, Battle, Card_shop, Deck_edit. 

#Temporary value
card_in_pack = 15
key_pressed = ""
card_un_pack = 0
# Main game loop

Game_init();
while True:
	colors = ["🚫","⚪","🔵","⚫","🔴","🟢"]; 

	if card_in_pack > 0:
		if key_pressed == "a":
			os.system('clear')
			card_in_pack -=1;
			card_un_pack +=1 ;
		print("📦["+str(card_in_pack)+"] "+"🎴"*card_un_pack);
		print("  [Info]--------------------------------------");
		card_name = str(players[0].deck[card_un_pack].name)
		card_power = str(players[0].deck[card_un_pack].power)
		card_taughness = str(players[0].deck[card_un_pack].taughness)
		card_cost = ""
		if players[0].deck[card_un_pack].cost[0]>0:
			card_cost += colors[0]+"["+str(players[0].deck[card_un_pack].cost[0])+"]"
		for x in range(len(players[0].deck[card_un_pack].cost)-1):
			card_cost += str(players[0].deck[card_un_pack].cost[x+1]*colors[x+1])
		card_name = str(players[0].deck[card_un_pack].name)
		print("Name: "+card_name)
		print("Name: "+card_power)
		print("Name: "+card_taughness)
		print("Name: "+card_cost)
	# Unpacking card test
	key_pressed = get_input();

	







