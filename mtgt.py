# Imports
from random import randrange
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
colors = ["[White ⚪]","[Blue 🔵]","Black ⚫","[RED 🔴]","[Green 🟢]","[Colorless 🚫]"]; # Not sure this will have a use case?

# Cursor selection	
class selection: 
	def __init__(self, x, y, over, selected):

# Class
## Cards class
### Creature, Land and other card type card class
### (Color cost could be stored in an array with five index of integer representing the color cost, and an extra index for the color less cost.)
class Card:
	def __init__(self, self_id, power, taughness, cost, card_type):
		self.self_id = self_id;
		self.attack = attack;
		self.deffence = deffence;
		self.type = card_type; # Sorcery, Land, Enchantment, Creature...
		self.kind = kind; # Human, Dinosaur Avatar, Vampire...
		self.cost = cost;
		self.name = namegenerator.gen();
		self.taped = False;
		
		# Make a function to calculate what color the card is based on the mana cost array.
		# IF, their is a need for it in the game otherwise just ignore it.
		self.color = color;
		
		#Calculate the total mana cost of the card
		for cost_index in range(len(this.cost)):
			total_cost+=this.cost[cost_index]
		self.total_cost = total_cost;	
		
# Player 
## (Don't forget to add an extra deck)	
## (You can use 2D array to stack card in the same place.)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	def __init__(self, name, self_id, deck, hand, health, mana_zone, field_zone, graveyard, Playable):
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
	
	def move_card(source, selected, destination):
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
	max_cost = 16
	min_cost = 1
	
	if ratio >= 6:
		# If all mana color including colorless are in the ratio, select a random value to each.
		# Limitation, the total mana cannot exceede 16.
		# not all 16 mana need to be used each time, quite the contrary.
		# to avoid this, each time we add a random value between 1 and 1+max_cost, we substract it from max_cost.
		# We then substract the result to our remaining cost to distribute.
		
		# Remove the minimum cost multiplied by the amounth of color index in the array. since it will be added by default
		max_cost -= min_cost * final_cost
		
		# Loop for each index of the final_cost.
		for cost_index in len(final_cost):
			current_cost = random.randint(0,max_cost)
			max_cost - current_cost
			final_cost[cost_index] = min_cost+current_cost; 
	
		# shuffle the cost array.
		random.shuffle(final_cost)
		
		return final_cost
	
	else:	
		# If NOT all mana color including colorless are in the ratio, select a random value to each equal to the ratio of color.
		# Limitation, the total mana cannot exceede 16.
		# to avoid this, each time we add a random value between 1 and 1+max_cost, we substract it from max_cost.
		# We then substract the result to our remaining cost to distribute.
		
		# Remove the minimum cost multiplied by the amounth of color index in the array. since it will be added by default
		max_cost -= min_cost * ratio
		
		# Loop for ratio amounth of index in the final_cost array and add a random value.
		for cost_index in ratio:
			current_cost = random.randint(0,max_cost)
			max_cost - current_cost
			final_cost[cost_index] = min_cost+current_cost; 
	
		# shuffle the cost array.
		random.shuffle(final_cost)
		
		return final_cost

# Generate deck
def gen_deck():
	temp_deck = []
	
	# for each player, Loop trough for each card in the deck and generate them, and append them to deck.
	for card in range(deck_size):
		
		#Calculate the total mana cost of the card
		new_cost = Generate_cost()
		for cost_index in range(len(new_cost)):
			total_cost+=new_cost[cost_index]
		
		# Generate 
		power = random(0,total_cost*2+round(total_cost/2))
		taughness = random(0,total_cost*2+round(total_cost/2))
		
		# Maximum value based on the following, online reference.
		# https://www.reddit.com/r/EDH/comments/ogiko4/low_cost_high_power_creatures/
		# power + taughness limit:
		# 5 for a 1 mana
		# 10 for a 2 mana
		# 12 for a 3 mana
		# 15 for a 4 mana
		# 18 for a 5 mana
		# These value and formula can be change in the limiters array if needed, to be more similar to the original game.
		# Some self adverse effect can also increase a card initial default power and taughness, to compensate.
		limiters = [5,10,12,15,18]
		cost_limit = limiters[Total_cost]
		
		# Function to regulate the somme of both powerr and taughness based on the mana cost
		# like while p+t > limit, random(0,1) if 1 p-1, esle t-1
		while power + taughness > cost_limit:
			# Choose what atribute to debuff.
			if random.randint(0,1) == 1:
				power-=1;
			else:
				taughness-=1;
		
		
			
		
		# To begin with all the card witll be creature.
		new_card = Card(power, taughness, new_cost, "creature")
		# append card to the temporary deck variable.
		temp_deck.append(new_card)
	
	return temp_deck
		
		
# Combine all visual element layout in a single string variable and print it to the terminal to display frame.
def draw_frame(top,mid,end):
	("Turn: ["++"]")
		
	print(frame)
	
# Initialise the game parameter
def Game_init():
	# Generate both player decks
	first_deck = gen_deck();
	second_deck = gen_deck();
	# Generate Players.
	#(name, self_id, deck, hand, health, mana_zone, field_zone, graveyard, Playable):
	players[0] = Player("Main_player",first_deck,initial_health,[],[],[], False)
	players[0] = Player("Ai_player",second_deck,initial_health,[],[],[], False)
	# Select who will start
	player_turn=random.randrange(0,1);
	

# Functions
## Return keypress input from curtsies
def get_input():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e
		
# color Cost ratio
def cost_ratio():
	
	# The ratio is based on 1 over the x_color_ratio value.
	# If the value is equal to 0 the card will have the following X amounth of color mana cost diversity.
	# Otherwise it will try the following ratio in order 
	# if none of the value return 0 then the card will be colorless.
	
	one_color_ratio = 4
	two_color_ratio = 6
	tree_color_ratio = 8
	four_color_ratio = 10
	five_color_ratio = 15
	six_color_ratio = 20
	
	if random.randrange(0,one_color_ratio) == 0:
		#One color attribute (excluding colorless)
		return 1
	elif random.randrange(0,two_color_ratio) == 0:
		#Two color attribute
		return 2
	elif random.randrange(0,tree_color_ratio) == 0:
		#Tree color attribute
		return 3
	elif random.randrange(0,four_color_ratio) == 0:
		#four color attribute
		return 4
	elif random.randrange(0,five_color_ratio) == 0:
		#five color attribute
		return 5
	elif random.randrange(0,six_color_ratio) == 0:
		#six color attribute (all color atribute, including colorless)
		return 6 
	else random.randrange(0,no_color_ratio) == 0: 
		#No color attribute
		return 0	
		
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
		
# Main game loop
while True:
	







