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
	while True:
		os.system('clear')
		# local variable
		creatures_zone = "";
		permanents_zone = "";
		lands_zone = "";
		hand = "";
		card_info="";
		cursor_symbol="🔍";
		
		# here should be AI side of the field
		# ---
		display_ai(ai,player,cursor_symbol);

		# display Player side of the field & the cursor -->
		
		# Creatyres ⬇️
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

		# Lands ⬇️
		for x in range(len(player.lands_zone)):
			if player.lands_zone[x] != None:
				for card in player.lands_zone[x]:
					if player.cursor_x == card and player.cursor_y == 3:
						lands_zone += cursor_symbol;
					else:
						lands_zone += str(card.symbol)		
		print(lands_zone)
			
		# Hand ⬇️
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
		
		# Actions input
		print("y:"+str(player.cursor_y)+" x:"+str(player.cursor_x))
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
				
	
#player, ai = initialisation();
#field();

## Return keypress input from curtsies
def get_input():
	#keynames='curses'
	with Input() as input_generator:
		for e in input_generator:
			return e
			
while True:
	key_pressed = get_input();
	print("pressed: "+str(key_pressed))



