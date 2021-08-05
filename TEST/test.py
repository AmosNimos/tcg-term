# It's all temporary for testing, i get sh!t done as fast as i can here.

import classes
import random
import os

# Vars
## Rules Variables
deck_size = 60;
initial_health = 20;
max_hand_size = 7;
cursor_symbol="@";

def initialisation():
	player = classes.Player("test", initial_health);
	player.gen_deck();
	player.draw(7)
	print(player.deck[random.randint(0,len(player.deck))].name)
	return player

def field():
	while True:
		os.system('clear')
		# local variable
		creatures_zone = "";
		permanents_zone = "";
		lands_zone = "";
		hand = "";
		card_info=""
		# here should be AI side of the field
		# ---

		# display Player side of the field & the cursor -->
		
		# Creatyres ⬇️
		for card in range(len(player.creatures_zone)):
			if player.cursor_x == card and player.cursor_y == 4:
				creatures_zone += cursor_symbol;
			else:
				creatures_zone += str(player.creatures_zone[card].symbol)
		print(creatures_zone)

		# Permanents ⬇️
		for card in player.permanents_zone:
			if player.cursor_x == card and player.cursor_y == 3:
				permanents_zone += cursor_symbol;
			else:
				permanents_zone += str(card.symbol)
		print(permanents_zone)

		# Lands ⬇️
		for card in player.lands_zone:
			if player.cursor_x == card and player.cursor_y == 2:
				lands_zone += cursor_symbol;
			else:
				lands_zone += str(card.symbol)
				
		print(lands_zone)

		# Hand
		for card in range(len(player.hand)):
			if player.cursor_y == 1 and len(player.hand)<1:
				player.cursor_y-=1;
			if player.cursor_x == card and player.cursor_y == 1:
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
		
		if player.cursor_y == 0:
			print(cursor_symbol+"["+str(len(player.deck))+"]")
		else:
			print("#["+str(len(player.deck))+"]")
		
		# Print Info
		print("-[Info]----------------------")
		print(card_info)
		
		# actions input
		print("y:"+str(player.cursor_y)+" x:"+str(player.cursor_x))
		action= input("Cursor:")
		
		# Place card
		if action == "use":
			selected = player.hand[player.cursor_x]
			if selected.supertype == "Creature":
				player.creatures_zone.append(selected);
				player.hand.pop(player.cursor_x); 
			else:
				player.lands_zone.append(selected);
				player.hand.pop(player.cursor_x); 
		
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
				
	
player = initialisation();
field();



