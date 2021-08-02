import classes
import random
# Vars
## Rules Variables
deck_size = 60;
initial_health = 20;
max_hand_size = 7;

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
	
	# here should be AI side of the field
	# ---
	
	# Player side of the field
	for card in player.creatures_zone:
		creatures_zone += str(card.symbol)
	print(creatures_zone)
	
	for card in player.permanents_zone:
		permanents_zone += str(card.symbol)
	print(permanents_zone)
	
	for card in player.lands_zone:
		lands_zone += str(card.symbol)
	print(lands_zone)
	
	for card in player.hand:
		hand += str(card.symbol)
	print(hand+"["+str(len(player.hand))+"]")
	
	print("#["+str(len(player.deck))+"]")
	
player = initialisation();
field();



