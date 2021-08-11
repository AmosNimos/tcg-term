# It's all temporary for testing, i get sh!t done as fast as i can here.

# summoning star "⍟✪⍟۞"

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

def field():
	# local variable
	console_text =""
	cursor_symbol="🔍";
	creatures_zone = "";
	permanents_zone = "";
	lands_zone = "";
	hand = "";
	card_info="";
	
	while True:
		os.system('clear')

		
		# here should be AI side of the field
		# ---
		display_ai(ai,player,cursor_symbol);

		# display Player side of the field & the cursor -->
		
		# Creatyres ⬇️
		creatures_zone= ""
		for card in range(len(player.creatures_zone)):
			if player.cursor_x == card and player.cursor_y == 5:
				creatures_zone += cursor_symbol;
			else:
				creatures_zone += str(player.creatures_zone[card].symbol)
		print(creatures_zone)

		# Permanents ⬇️
		for card in player.permanents_zone:
			if player.cursor_x == card and player.cursor_y == 4:
				permanents_zone += cursor_symbol;
			else:
				permanents_zone += str(card.symbol)
		print(permanents_zone)

		# display lands_zone ⬇️
		lands_zone= "" # reset string
		for x in range(len(player.lands_zone)):
			if player.lands_zone[x] != None:
				for card in player.lands_zone[x]:
					if player.cursor_x == card and player.cursor_y == 3:
						lands_zone += cursor_symbol;
					else:
						lands_zone += str(card.symbol)		
		print(lands_zone)
			
		# display hand ⬇️
		hand="" # reset string
		for card in range(len(player.hand)):
			if player.cursor_y == 1 and len(player.hand)<1:
				player.cursor_y-=1;
			if player.cursor_x == card and player.cursor_y == 2:
				hand += cursor_symbol; 
				if(player.hand[card].supertype == "Creature"):
					card_info = "Name:"+ str(player.hand[card].name) + "\n" 
					card_info += "Cost:"+ str(player.hand[card].cost) + "\n"
					card_info += player.hand[card].supertype + "\n"
					card_info += "Rarity:" + str(player.hand[card].rarity) + "\n"
					card_info += "Effect: [...]\n"
					card_info += "Power:[" + str(player.hand[card].power) + "]\n"
					card_info += "Power:[" + str(player.hand[card].taughness) + "]\n"
				else:
					card_info = "Name:"+ str(player.hand[card].name) + "\n"
					card_info += player.hand[card].supertype + "\n"		
			else:
				hand += str(player.hand[card].symbol)
		print(hand+"["+str(len(player.hand))+"]")
		
		# Graves
		if player.cursor_y == 1:
			print(cursor_symbol+"["+str(len(player.graveyard))+"]")
		else:
			print("💀["+str(len(player.graveyard))+"]")
			
		# Deck
		if player.cursor_y == 0:
			print(cursor_symbol+"["+str(len(player.deck))+"]")
		else:
			print("⬜["+str(len(player.deck))+"]")
		
		# Print Info
		print("-[Info]----------------------")
		print(card_info)
		
		# Cursor location
		print("y:"+str(player.cursor_y)+" x:"+str(player.cursor_x))
			
		# Print Console
		print(console_text)	
		
		key_pressed = get_input();
		if key_pressed == "w":
			player.cursor_y += 1;
			console_text = ""
		if key_pressed == "a":
			player.cursor_x -= 1;
			console_text = ""
		if key_pressed == "s":
			player.cursor_y -= 1;
			console_text = ""
		if key_pressed == "d":
			player.cursor_x += 1;
			console_text = ""
		if key_pressed == "h":	
			console_text = "Summoning " + str(player.hand[player.cursor_x].name)
			selected = player.hand[player.cursor_x]
			selected.summon(player);
		if key_pressed == "j":	
			console_text = "Draw" 
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




