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

#Zones y Index
graveyard_y=0;
deck_y=1;
hand_y=2;
land_y=3;
permanent_y=4;
creature_y=5;

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
		#display_ai(ai,player,cursor_symbol);

		# display Player side of the field & the cursor -->
		
		## Display Zones >>
		
		# Creatures ⬇️
		if len(player.creatures_zone)>0:
			creatures_zone= ""
			for card in range(len(player.creatures_zone)):
				if player.cursor_x == card and player.cursor_y == creature_y:
					creatures_zone += cursor_symbol;
				else:
					creatures_zone += str(player.creatures_zone[card].symbol)
			print(creatures_zone)
		elif player.cursor_y == creature_y:
			player.cursor_y = deck_y

		# Permanents ⬇️
		if len(player.permanents_zone)>0:
			for card in player.permanents_zone:
				if player.cursor_x == card and player.cursor_y == permanent_y:
					permanents_zone += cursor_symbol;
				else:
					permanents_zone += str(card.symbol)
			print(permanents_zone)
		elif player.cursor_y == permanent_y:
			player.cursor_y = creature_y
			
		# Lands ⬇️
		# count lands
		lands_count=0;
		for x in range(len(player.lands_zone)):
			lands_count += len(player.lands_zone[x])
		#player.console_text = "lands:"+str(lands_count)
		if lands_count>0:
			lands_zone= "" # reset string
			land_index = 0;
			#Wrap the cursor
			if player.cursor_y == land_y:
				if player.cursor_x<0:
					player.console_text = "lands:"+str(lands_count)
					player.cursor_x=lands_count-1;
				if player.cursor_x>lands_count-1:
					player.console_text = "lands:"+str(lands_count)
					player.cursor_x = 0
			for x in range(len(player.lands_zone)):
				if player.lands_zone[x] != None:
					for card in player.lands_zone[x]:
						if player.cursor_x == land_index and player.cursor_y == land_y:
							land_index +=1
							lands_zone += str(cursor_symbol);
						else:
							land_index +=1
							lands_zone += str(card.symbol)
			print(lands_zone)
		elif player.cursor_y == land_y:
			player.cursor_y = permanent_y
			
		# display hand ⬇️
		if len(player.hand)>0:
			hand="" # reset string
			# wrap the cursor 
			if player.cursor_y == hand_y:
				if player.cursor_x>len(player.hand)-1:
					player.cursor_x=0;
				if player.cursor_x<0:
					player.cursor_x=len(player.hand)-1;
			for card in range(len(player.hand)):
				if player.cursor_y == hand_y and len(player.hand)<1:
					player.cursor_y=deck_y;
				if player.cursor_x == card and player.cursor_y == hand_y:
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
		if len(player.graveyard)>0:
			if player.cursor_y == graveyard_y:
				player.cursor_x = 0;
				print(cursor_symbol+"["+str(len(player.graveyard))+"]")
			else:
				print("💀["+str(len(player.graveyard))+"]")
		elif player.cursor_y == graveyard_y:
			player.cursor_y = deck_y
			
		# Deck
		if player.cursor_y == deck_y:
			player.cursor_x = 0;
			print(cursor_symbol+"["+str(len(player.deck))+"]")
		else:
			print("⬜["+str(len(player.deck))+"]")
		
		# Print Info
		print("-[Info]----------------------")
		print(card_info)
		
		# Cursor location
		print("y:"+str(player.cursor_y)+" x:"+str(player.cursor_x))
			
		# Print Console
		print(player.console_text)	
		
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
			player.console_text = "Summoning " + str(player.hand[player.cursor_x].name)
			selected = player.hand[player.cursor_x]
			selected.summon(player);
		if key_pressed == "j":	
			player.console_text = "Draw" 
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




