# It's all temporary for testing, i get sh!t done as fast as i can here.

import classes
import random
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
	# local variable
	creatures_zone = "";
	permanents_zone = "";
	lands_zone = "";
	hand = "";
	
	while true:
		# here should be AI side of the field
		# ---

		# display Player side of the field & the cursor
		for card in range(player.creatures_zone):
			if player.cursor_x == card and player.cursor_y == 0:
				creatures_zone += str(player.symbol)
			else:
				creatures_zone += cursor_symbol;
		print(creatures_zone)

		for card in player.permanents_zone:
			if player.cursor_x == card and player.cursor_y == 0:
				permanents_zone += str(card.symbol)
			else:
				permanents_zone += cursor_symbol;
		print(permanents_zone)

		for card in player.lands_zone:
			if player.cursor_x == card and player.cursor_y == 0:
				lands_zone += str(card.symbol)
			else:
				lands_zone += cursor_symbol;
		print(lands_zone)

		for card in player.hand:
			if player.cursor_x == card and player.cursor_y == 0:
				hand += str(card.symbol)
			else:
				hand += cursor_symbol;
		print(hand+"["+str(len(player.hand))+"]")

		if player.cursor_y == 0:
			print("#["+str(len(player.deck))+"]")
		else:
			print(cursor_symbol+"["+str(len(player.deck))+"]")
		movement = input("Cursor:")
		if movement[0] == "y":
			player.cursor_y += movement[1];
		elif movement[0] == "x":
			player.cursor_x += movement[1];
	
player = initialisation();
field();



