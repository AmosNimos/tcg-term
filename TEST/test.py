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
		
		# Count lands
		lands_count=0;
		for x in range(len(player.lands_zone)):
			lands_count += len(player.lands_zone[x])
		if lands_count>0:
			highest_zone = land_y;
			
		## Display Zones >>
		
		# Wrap Cursor on the y axis >>
		
		# If a zone is empty replace it with the one above
		# I know, this is verry big brain move.
		if(len(player.permanents_zone)==0):
			creature_y=4;
		else: 
			highest_zone=4;
			
		
		if len(player.permanents_zone)>0 and len(player.creatures_zone)>0 and len(player.hand_zone)>0:
			highest_zone=5;
		elif len(player.permanents_zone)>0 or len(player.creatures_zone)>0:
			highest_zone=4;
			
		if player.cursor_y > highest_zone:
			player.cursor_y = lowest_zone;
		if player.cursor_y < lowest_zone:
			player.cursor_y = highest_zone;
		
		# Creatures ⬇️
		if len(player.creatures_zone)>0:
			highest_zone = creature_y;
			if player.cursor_y == creature_y:
				# Wrap the cursor 
				if player.cursor_x>len(player.creatures_zone)-1:
					player.cursor_x=0;
				if player.cursor_x<0:
					player.cursor_x=len(player.creatures_zone)-1;
				
			creatures_zone= ""
			for card in range(len(player.creatures_zone)):
				if player.cursor_x == card and player.cursor_y == creature_y:
					creatures_zone += cursor_symbol;
					card_info = str(player.creatures_zone[card].info());
				else:
					creatures_zone += str(player.creatures_zone[card].symbol)
			print(creatures_zone)


		# Permanents ⬇️
		if len(player.permanents_zone)>0:
			for card in player.permanents_zone:
				if player.cursor_x == card and player.cursor_y == permanent_y:
					permanents_zone += cursor_symbol;
				else:
					permanents_zone += str(card.symbol)
			print(permanents_zone)
			
		# Lands ⬇️
		#player.console_text = "lands:"+str(lands_count)
		if lands_count>0:
			lands_zone="" # reset string
			land_index=0;
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
							card_info = str(card.info());
						else:
							land_index +=1
							lands_zone += str(card.symbol)
			print(lands_zone)
			
		# Tapped_lands ⬇️
		tapped_zone = ""
		if len(player.tapped_lands)>0
			for card in player.tapped_lands:
				if player.cursor_y == t_land_y:
					tapped_zone+=str(cursor_symbol);
				else:
					tapped_zone+=card.symbol;
			print(tapped_zone)
			
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
					card_info = str(player.hand[card].info());	
				else:
					hand += str(player.hand[card].symbol);
			print(hand+"["+str(len(player.hand))+"]");
			
		# Deck
		if len(player.deck)<=0:
			player.game_over=True;
		else:
			if player.cursor_y == deck_y:
				player.cursor_x = 0;
				print(cursor_symbol+"["+str(len(player.deck))+"]")
			else:
				print("⬜["+str(len(player.deck))+"]")
				
		# Graves
		if player.cursor_y == graveyard_y:
			player.cursor_x = 0;
			print(cursor_symbol+"["+str(len(player.graveyard))+"]")
		else:
			print("💀["+str(len(player.graveyard))+"]")
		
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




