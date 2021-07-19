# mtg-term
A minimalistic pen source mtg-like game made in python that can be played on a terminal emulator.

## Project state:

Incomplete, In development

# Main Game View
 
 ~~~
 Turn: [Player_name_one]
 Phase: [Beginning/Untap Step] 

 ▶️ [Player_name_one]: Health[20] Deck[60]
 
 Hand:  🔳🔳🔳🔳🔳🔳🔳[7] 
 Graveyard: 💀[0]
 
 Mana:  🟪 ⬛⬛
 Field: 🟫🟫 ⬛
        🗡️
        🛡️        
 Field: 🟫🟫🟫
 Mana:  🟪🟪 ⬛
 
 Graveyard: 💀[6]
 Hand:  🟧🟫🟪🟫🔍🟧[6]
 
 [Player_name_two]: Health[20] Deck[60]
 
 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: 🔵🔵🔵[3] 🚫🚫[2]
 Type: Creature
 Effect: [ ... ]
 P&T: [1/1]
 ~~~
 
 # Graveyard Game View
  
 ~~~
 [Player_name_one] 
 Graveyard: 🟧🟫🟪🟫🔍🟧[6]
 Field: ⚔️
 
 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: 🔵🔵🔵[3] 🚫🚫[2]
 Type: Creature
 Effect: [ ... ]
 P&T: [1/1]
 ~~~
  
 
 
 # Symbols emoji and therm used
 
 ~~~
 Symbols:
 Tapped ⬛
 Artefact Or Enchantment ⬜
 Creature 🟫
 Instant or Sorcery 🟧
 Cursor/Slection 🔍
 Colorless +
 Attacking 🗡️
 Blocking 🛡️
 Colorless 🚫
 Mana card 🟪
 Back 🔳
 
 Therm: P&T = Power and Taughness
 ~~~
 
 # Info on phase and stuff
 ~~~
 https://www.youtube.com/watch?v=V4rYwsBMKxs
 Phase: beginning, first_main, combat, second_main, ending
 Steps: Beginning(Untap, Draw) Main(Land, Spells) Combat(Attackers, Blockers, damage) Second(Land, Spells) Ending(Cleanup)
 ~~~
 


