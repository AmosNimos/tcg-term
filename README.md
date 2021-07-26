## Project state:
🔧 🚧🚧🚧 Incomplete, In development 🚧🚧🚧 👷
(Keep in mind that at the moment, This project is currently undone, and will not work, if you try to lunch it.)

# What is mtg-term?
It is a minimalistic, open-source, mtg-like game, made in python, that can be played on most terminal emulator on linux.
The first goal to be realistic in scope, is to have a playable single player game, with simple generated card, that have simple [__Keyword ability__](https://mtg.fandom.com/wiki/Keyword_ability) effect. Then once completed, add complexity progressivelly, and maybe in the far long distant future a form of multiplayer.

![Magic](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallup.net%2Fwp-content%2Fuploads%2F2016%2F04%2F10%2F315469-Magic_The_Gathering-fantasy_art-heroes-warrior.jpg&f=1&nofb=1)

[blueprint Guide](https://mtg.fandom.com/wiki)

# Main Game View
 > I am still not sure what is the best way to display the mana cost.
 ~~~
 Turn: [Player_name_one]
 Phase: [Beginning/Untap Step] 

 ▶️ [Player_name_one]: Health[20] Deck[60]
 
 Hand:  🔳🔳🔳🔳🔳🔳🔳[7] 
 Graveyard: 💀[0]
 
 Mana:  🟪 ⬛⬛
 Field: 🟫🟫[2] ⬛
        🗡️
        🛡️        
 Field: 🟫🟫🟫
 Mana:  🟪🟪 ⬛
 
 Graveyard: 💀[6]
 Hand:  🟧🟫🟪🟫🔍🟧[6]
 
 [Player_name_two]: Health[20] Deck[60]
 
 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: 🚫[2] 🔵🔵🔵 
 Type: Creature
 Rarity: Mythic rare 🌟
 Effect: [ ... ]
 Power: 🗡️[1]
 Taughness: 🛡️[1]
 ~~~
 
 # Deck Edit
 ~~~
Filter: Name[🅰] Cost[🪙] Power[🗡️] Taughness[🛡️] Color[🚫]
[Deck]
🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫
🟫🟫🟫🟫🔍🟫🟫🟫🟫🟫
🟫🟫🟫🟫🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟪🟪🟪🟪🟪🟪🟪
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
🟪🟪🟪🟪🟪🟪🟪

[Sideboard]
🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫
🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫
🟫🟫🟫🟫🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟪🟪🟪🟪🟪🟪🟪
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
🟪🟪🟪🟪🟪🟪🟪

 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: 🚫🚫[2] 🔵🔵🔵[3]
 Type: Creature
 Rarity: Mythic rare 🌟
 Effect: [ ... ]
 Power: 1
 taughness: 1
 Copy: 3/4
 
❌[REMOVE] 👥[Duplicate][Cost: 1000🪙]
 -----------------------------
 
🚪[MAIN MENU]
~~~

 ~~~
 [Player_name_one] 
 Graveyard: 🟧🟫🟪🟫🔍🟧[6]
 Field: ⚔️
 
 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: 🚫[2] 🔵[3]
 Type: [Creature]
 Effect: [ ... ]
 P/T: [1/1]
 ~~~
  
 # Card shop view
 
 > Don't worry you buy the cards with in game point, which can be won by winning game.
 > No ingame purchasses XD
~~~
[Cards: 15x]:
  📦[🚫][Cost: 150🪙]
  📦[⚪][Cost: 250🪙]
🔍 📦[🔵][Cost: 250🪙]
  📦[⚫][Cost: 250🪙]
  📦[🔴][Cost: 250🪙]
  📦[🟢][Cost: 250🪙]
 
  🚪[MAIN MENU]
~~~

# Settings view
~~~
Settings:
 🔍 Text Only [Off]
 ⚙️ Sound Effect [Off]
 ⚙️ Text Color [On]
 
 🚪[MAIN MENU]
 
~~~

 
 # Symbols emoji and therm used
 
 ~~~
 Symbols:
 Tapped ⬛
 Creature 🟫
 Instant or Sorcery Or Artefact Or Enchantment 🟧
 Cursor/Slection 🔍 (Alternative cursor idea 👇👆👉🤚💠 )
 Colorless +
 Attacking 🗡️
 Blocking 🛡️
 Colorless 🚫
 Mana card 🟪
 Back 🔳
 Mytic Rare 🌟
 Rare ⭐
 Uncomun 🥇
 
 I also found these character emoji: 🧙🧙‍♀️🧙‍♂️🧝🧝‍♀️🧝‍♂️🧛🧛‍♀️🧛‍♂️🧟🧟‍♀️🧟‍♂️

 
 
 Therm: P&T = Power and Taughness
 ~~~
 
 # Game default key bindings 🖱️⌨️
 
 ~~~
 
 ## An option to customise or swap these default key bindings should be profided in the form of a config file or settings page, eventually.
 
 # Controlle options
 w = want selection (select what is selected by the cursor)
 a = action (attacking/blocking/activating a spell)
 s = skip (will skip to the next phase)
 d = end turn (will skip all remaining phases)
 
 # Move cursor
 h = left
 j = down
 k = up
 l = right
 
 ~~~
 
 # Info on phase and stuff
 ~~~
 https://www.youtube.com/watch?v=V4rYwsBMKxs
 Phase: beginning, first_main, combat, second_main, ending
 Steps: Beginning(Untap, Draw) Main(Land, Spells) Combat(Attackers, Blockers, damage) Second(Land, Spells) Ending(Cleanup)
 ~~~
 
# Help Needed!
I really want to play an mtg-like alternative game on linux, so please do your best to contribute if you can!
Read the task-list to see the priority.
This project only accept clear, organized and well commented code.
You can also submit suggestion and idea, as long as they are unambiguous and well developed.

![WE NEED YOU](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.fau.edu%2Fsas%2Fimages%2FSAS%2520Volunteer%2520sign11.jpg&f=1&nofb=1)

> You feedback is welcome.


