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
deckSize = 60;
initial_health = 20;

# Game Variables 
colorless = "🔷";
colors = ["[White ⚪]","[Blue 🔵]","Black ⚫","[RED 🔴]","[Green 🟢]"];

# Class
## Cards class
### Creature, Land and other card type card class
### (Color cost could be stored in an array with five index of integer representing the color cost, and an extra index for the color less cost.)

class Card:
	def __init__(self, self_id, attack, deffence, color, cost, card_type):
		self.self_id = self_id;
		self.attack = attack;
		self.deffence = deffence;
		self.color = color;
		self.type=card_type; # Sorcery, Land, Enchantment, Creature...
		self.kind=kind; # Human, Dinosaur Avatar, Vampire...
		self.cost = cost;
		self.name = namegenerator.gen();
		self.taped = False;
	
	
# Cursor selection	
class selection: 
	def __init__(self, x, y, over, selected):		
# Player 
## (Don't forget to add an extra deck)	
## (You can use 2D array to stack card in the same place.)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	def __init__(self, self_id, deck, hand, health, mana_zone, field_zone, graveyard):
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
		
class Field:
	def __init__(self, mana):

def draw_frame(top,mid,end):
	frame = top + mid + end;
	print(frame)

# Functions
## Return keypress input from curtsies
def get_input():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

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
	







