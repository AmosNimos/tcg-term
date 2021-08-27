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

# Vars
## Rules Variables
deck_size = 60;
initial_health = 20;
max_hand_size = 7;
room = "menu"

## Return keypress input
def get_input():
	#keynames='curses'
	with Input() as input_generator:
		for e in input_generator:
			return e

def initialisation():

	menu = classes.menu();

	# gen player 
	player = classes.Player("test", initial_health);
	player.gen_deck();
	player.draw(7)
	
	# gen ai
	ai = classes.AI("test", initial_health);
	ai.gen_deck();
	ai.draw(7)
	# gen ai
	
	return player, ai, menu


# This function is for displaying the field page on the screen	
def field():
	
	while True:
		os.system('clear')

		
		# here should be AI side of the field
		# ---
		#display_ai(ai,player,cursor_symbol);

		# display Player side of the field & the cursor -->
		if menu.room == 0:
			menu.display(player)
		else:
			player.display_field();
		
		
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
			if player.cursor_y == player.hand_y:
				selected = player.hand[player.cursor_x];
			elif player.cursor_y == player.bench_y: 
				selected = player.bench_zone[player.cursor_x];
			player.summon(selected);
		if key_pressed == "j":	
			selected = player.draw();
	
player, ai, menu = initialisation();
field();




