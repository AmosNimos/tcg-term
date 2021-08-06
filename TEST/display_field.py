def display_ai(ai,player,cursor_symbol):

		# local variable
		creatures_zone = "";
		permanents_zone = "";
		lands_zone = "";
		hand = "";
		card_info="";
	
		# Deck
		if player.cursor_y == 10:
			print(cursor_symbol+"["+str(len(player.deck))+"]")
		else:
			print("⬜["+str(len(player.deck))+"]")

		# Gravess
		if player.cursor_y == 9:
			print(cursor_symbol+"["+str(len(ai.graveyard))+"]")
		else:
			print("💀["+str(len(ai.graveyard))+"]")
		
		# Hand ⬇️
		for card in range(len(ai.hand)):
			if player.cursor_y == 1 and len(ai.hand)<1:
				player.cursor_y-=1;
			if player.cursor_x == card and player.cursor_y == 8:
				hand += cursor_symbol; 
				if(ai.hand[card].supertype == "Creature"):
					card_info = "Name:"+ str(ai.hand[card].name) + "\n" 
					card_info += "Cost:"+ str(ai.hand[card].cost) + "\n"
					card_info += ai.hand[card].supertype + "\n"
					card_info += "Rarity:" + str(ai.hand[card].rarity) + "\n"
					card_info += "Effect: [...]\n"
					card_info += "Power:[" + str(ai.hand[card].power) + "]\n"
					card_info += "Power:[" + str(ai.hand[card].taughness) + "]\n"
				else:
					card_info = "Name:"+ str(ai.hand[card].name) + "\n"
					card_info += ai.hand[card].supertype + "\n"
			else:
				hand += str(ai.card_back)
		print(hand+"["+str(len(ai.hand))+"]")

		# Lands ⬇️
		for card in ai.lands_zone:
			if player.cursor_x == card and player.cursor_y == 7:
				lands_zone += cursor_symbol;
			else:
				lands_zone += str(ai.card_back)		
		print(lands_zone)

		# Permanents ⬇️
		for card in ai.permanents_zone:
			if player.cursor_x == card and player.cursor_y == 6:
				permanents_zone += cursor_symbol;
			else:
				permanents_zone += str(ai.card_back)
		print(permanents_zone)
		
		# Creatyres ⬇️
		for card in range(len(ai.creatures_zone)):
			if player.cursor_x == card and player.cursor_y == 5:
				creatures_zone += cursor_symbol;
			else:
				creatures_zone += str(ai.card_back)
		print(creatures_zone)


