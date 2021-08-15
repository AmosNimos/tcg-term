# TCG-TERM
![open_TCG_img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F699740%2Fpexels-photo-699740.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26fit%3Dcrop%26h%3D627%26w%3D1200&f=1&nofb=1)

## Project state:
🔧 🚧🚧🚧 Incomplete, In development 🚧🚧🚧 👷

(Keep in mind that at the moment, This project is currently undone, and will not work, if you try to lunch it.)

> Latest prototype of this project are in the TEST directory which like the name imply is for testing and development purposes.

> Once the TEST directory has a working prototype, i will start to refine it, by making more generalise function that have more flexibility, i will separate most of the code in their own function & modual.

I will probably Reuse some code and thechnics from this previus project of mine.
It was a verry similar project, and i learn a lot from making it, even do I try to keep this project simple, i do not whish to rush it, and i do not have that much free time to work on it, so things can take some time to take shape.

[RAND-CARD](https://github.com/AmosNimos/rand-card)

# What is tcg-term?
It started as a project to make an mtg alternative game on the linux terminal, but i now aim to include other style of tcg game play mode while avoiding to enfringe on the copy rightable content. 

It is a minimalistic, open-source, tcg-like game, made in python, that can be played on most terminal emulator on linux.
The first goal to be realistic in scope, is to have a playable single player game, with simple generated card, that have simple [__Keyword ability__](https://mtg.fandom.com/wiki/Keyword_ability) effect. Then once completed, add complexity progressivelly, and maybe in the far long distant future a form of multiplayer.

3 main gamemode "inspired" by:
- magic
- pokemon
- yu-gi-oh

> And maybe a gamemode called __Battle-Cry__ ( Another one of my open source project Here on Github. )

[blueprint Guide](https://mtg.fandom.com/wiki)

# Main Game View
 > I am still not sure what is the best way to display the mana cost.
 > C: Creatures, P: Permanents, L: Lands.
 > D: Deck, H: Hand, G: Graveyard.
 ~~~
 Turn: [Player_name_one]
 Phase: [Beginning/Untap Step] 

 ▶️ [Player_name_one]: Health[20]
 
 D: ⬜[60]
 G: 💀[0]
 H: 🔳🔳🔳🔳🔳🔳🔳[7] 
 
L: 🟪 ⬛⬛
P: 🟧
C: 🟫 🟫[2] ⬛
   🗡️
     🛡️🛡️        
C: 🟫🟫🟫
P: 🟧🟧
L: 🟪🟪 ⬛
 
H: 🟧🟫🟪🟫🔍🟧[6]
G: 💀[6]
D: ⬜[60]
 
 [Player_name_two]: Health[20] 
 
 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: 🚫[2] 🔵🔵🔵 
 Type: Creature
 Rarity: Mythic rare 🌟
 Effect: [ ... ]
 Power: 🗡️[1]
 Taughness: 🛡️[1]
 ~~~
 
 ## Text-only
 ~~~
 Turn: [Player_name_one]
 Phase: [Beginning/Untap Step] 

 > [Player_name_one]: Health[20] Deck[60]
 
 Hand:  #######[7] 
 Graveyard: [0]
 
L: # %%
P: #
C: # #[2] %
   A
    BB        
C: ###
P: ##
L: ## %
 
 Graveyard: [6]
 Hand:  ####@#[6]
 
 [Player_name_two]: Health[20] Deck[60]
 
 -[Info]----------------------
 Name: [Lorem Ipsum]
 Cost: None[2] Blue[3] 
 Type: Creature
 Rarity: Mythic rare *
 Effect: [ ... ]
 Power: 1
 Taughness: 1
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
 
# Help Needed!
I really want to play an tcg-like alternative game on linux, so please do your best to contribute if you can!


Read the task-list to see the priority.
This project only accept clear, organized and well commented code.
You can also submit suggestion and idea, as long as they are unambiguous and well developed.

![WE NEED YOU](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.fau.edu%2Fsas%2Fimages%2FSAS%2520Volunteer%2520sign11.jpg&f=1&nofb=1)

> You feedback is welcome.


