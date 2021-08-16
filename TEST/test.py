#ToDo!
"""
Make the following function
(If a zone is empty replace it with the one above.)
Make all zone 1d array?. 
(devise land in multiple 1d to then add them together when printing.
Add a zone for tapped Creature
Add a zone for tapped Lands
Make it so that color less mana can be used instead of a color specific mana
Make a function to return tapped lands from tapped_lands zone to the regular lands_zone
Maybe put tap creatures and tap lands in the same array?
"""


# It's all temporary for testing, i get sh!t done as fast as i can here.

# Non emoji
# summoning star "⍟✪۞✦✧★☆✯✡︎✩✫✬✭✮✶✷✵✸✹"
# card "🂠"
# Dice "⚀ ⚁ ⚂ ⚃ ⚄ ⚅"
# Cursor "➔" 

# Emoji symbol
# "🌀🔳🔲🔘↩️"

import classes
import random
import os
#from curties import Input
from key_input.key_input import Input

from display_field import display_ai

# Vars
## Rules Variables
deck_size = 60;
initial_health = 20;
max_hand_size = 7;

## Return keypress input
def get_input():
	#keynames='curses'
	with Input() as input_generator:
		for e in input_generator:
			return e

def initialisation():
	# gen player 
	player = classes.Player("test", initial_health);
	player.gen_deck();
	player.draw(7)
	
	# gen ai
	ai = classes.AI("test", initial_health);
	ai.gen_deck();
	ai.draw(7)
	# gen ai
	
	return player, ai


# This function is for displaying the field page on the screen	
def field():
	# local variable
	cursor_symbol="🔍";
	creatures_zone = "";
	permanents_zone = "";
	lands_zone = "";
	hand = "";
	card_info="";
	
	#Zones y Index
	graveyard_y=0;
	deck_y=1;
	hand_y=2;
	t_land_y=3;
	land_y=4;
	permanent_y=5;
	t_creature_y=6;
	creature_y=7;
	highest_zone = hand_y;
	lowest_zone = graveyard_y;
	
	while True:
		os.system('clear')

		
		# here should be AI side of the field
		# ---
		#display_ai(ai,player,cursor_symbol);

		# display Player side of the field & the cursor -->
		
		key_pressed = get_input();
		if key_pressed == "w":
			player.cursor_y += 1;
			player.console_text = ""
		if key_pressed == "a":
			player.cursor_x -= 1;
			player.console_text = ""
		if key_pressed == "s":
			player.cursor_y -= 1;
			player.console_text = ""
		if key_pressed == "d":
			player.cursor_x += 1;
			player.console_text = ""
		if key_pressed == "h":
			selected = player.hand[player.cursor_x]
			selected.summon(player);
		if key_pressed == "j":	
			selected = player.draw();
	
player, ai = initialisation();
field();
			
def action_system():
# Action input system
	action= input("Cursor:")
	
	# Place card
	if action == "summon":
		selected = player.hand[player.cursor_x]
		selected.summon(player);

	
	# Movements 
	if action[0] == "y":
		if action[1] == "+":
			player.cursor_y += int(action[2]);
		elif action[1] == "-":
			player.cursor_y -= int(action[2]);
		elif action[1] == "=":
			player.cursor_y = int(action[2]);
	elif action[0] == "x":
		if action[1] == "+":
			player.cursor_x += int(action[2]);
		elif action[1] == "-":
			player.cursor_x -= int(action[2]);
		elif action[1] == "=":
			player.cursor_x = int(action[2]); 




