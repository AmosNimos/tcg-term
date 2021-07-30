# Player 
## (You can use 2D array to stack card in the same place. and display the amounth of copy with a [x] after the card symbol)
### (Might be a better idea to separate the field variable from the player class init function.)
class Player:
	#side_board = []
	collection = [],
	coin = 0,
	hand = [],
	mana_zone = [],
	field_zone = [], 
	graveyard = [],
	def __init__(self, name, self_id, deck, health, hand_size):
		self.name = "Bob Smith",
		self.self_id = self_id,
		self.deck = deck,
		self.hand = hand,
		self.health = health,
		
class AI:
	def __init__(self, name, self_id, deck, health, hand_size):
		
