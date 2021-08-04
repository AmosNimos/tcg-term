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
		# here should be AI side of the field
		# ---

		# display Player side of the field & the cursor
		for card in range(len(player.creatures_zone)):
			if player.cursor_x == card and player.cursor_y == 4:
				creatures_zone += str(player.symbol)
			else:
				creatures_zone += cursor_symbol;
		print(creatures_zone)

		for card in player.permanents_zone:
			if player.cursor_x == card and player.cursor_y == 3:
				permanents_zone += str(card.symbol)
			else:
				permanents_zone += cursor_symbol;
		print(permanents_zone)

		for card in player.lands_zone:
			if player.cursor_x == card and player.cursor_y == 2:
				lands_zone += str(card.symbol)
			else:
				lands_zone += cursor_symbol;
		print(lands_zone)

		for card in range(len(player.hand)):
			if player.cursor_x == card and player.cursor_y == 1:
				hand += cursor_symbol; 
			else:
				hand += str(player.hand[card].symbol)
		print(hand+"["+str(len(player.hand))+"]")

		if player.cursor_y == 0:
			print("#["+str(len(player.deck))+"]")
		else:
			print(cursor_symbol+"["+str(len(player.deck))+"]")
			
		# Movement input
		print("y:"+str(player.cursor_y)+" x:"+str(player.cursor_x))
		movement = input("Cursor:")
		if movement[0] == "y":
			if isinstance(movement[1], int):
				player.cursor_y += int(movement[1]);
			elif movement[1] == "+":
				player.cursor_y += int(movement[2]);
			elif movement[1] == "-":
				player.cursor_y -= int(movement[2]);
		elif movement[0] == "x":
			if isinstance(movement[1], int):
				player.cursor_x += int(movement[1]);
			elif movement[1] == "+":
				player.cursor_x += int(movement[2]);
			elif movement[1] == "-":
				player.cursor_x -= int(movement[2]);
	
player = initialisation();
field();



