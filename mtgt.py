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
initial_health = 20

# Game Variables 
colors = ["[RED 🔴]","[Green 🟢]","[White ⚪]","Black ⚫","[Blue 🔵]"];

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
		self.type=card_type;
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

# Main game loop
while True:
	







