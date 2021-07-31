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
	print(player.deck[random.randint(0,len(player.deck))].name)
	
initialisation();



