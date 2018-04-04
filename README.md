# PythonMicroProject

#### Dungeon Game
---

#### Team: R-Py-G
##### Rachel Ashburn, Colleen Britt, Daniel Flynt, Patrick Messina
---

#### Overview
This dungeon game consists of a maze that the player must traverse, and along the way are monsters that the player must fight. Python 3.6 was used to implement the game. Travis was used to test the game.
***

#### Gameplay Instructions
* The player begins at the lower left corner.
* The exit is at the upper right corner.
* The player's goal is to reach the exit.
* Player must use WASD to move to the next tile.
---

#### Implementation
- [x] Map Generaton (Tiles)
- [x] Valid Player Movement
- [ ] Random Monster Placement
- [ ] Battle System
- [ ] Stats for Player and Monsters
=======
# PythonMicroProject

#### Maze Game
---

#### Team: R-Py-G
##### Rachel Ashburn, Colleen Britt, Daniel Flynt, Patrick Messina
---

#### Overview
This is a simple maze game. The player must reach the end to win.
Python 3.6 was used to implement the game.
***

#### Gameplay Instructions
* The player begins at the lower left corner.
* The exit is at the upper right corner.
* The user's goal is to reach the exit.
* The user must use WASD to move to the next tile.
---

#### Implementation
- [x] Map Generaton (Tiles)
- [x] Valid Player Movement
- ~~[ ] Random Monster Placement~~
- ~~[ ] Battle System~~
- ~~[ ] Stats for Player and Monsters~~

#### Progress Report

##### First Iteration

We decided to create a dungeon game. The idea for this dungeon game was that the user would traverse the maze and battle monsters along the way.

Daniel created a Game object for the board, which represents the maze. It was designed to allow the user to choose the size of the board when the player runs the game. The minimum acceptable size of the board was 5x5. To run the program, the user is required to type: python3 game.py <size of the width> <size of height>. The boundaries and walls were predefined no matter the chosen size of the board. On the board, "1" defines a valid path, and "0" defines the boundaries and walls (an invalid space). "2" represents the player. The start and finish tiles were also predefined.

Colleen implemented the user movement for the game. From the command-line, the game asks the user where they would like to move, and the user must use lowercase or uppercase WASD keys to move. The algorithm determines whether the player's chosen move is valid or not. If it is valid, the "2" is moved to the position and the previous tile is still defined as a valid space. If it is invalid, the "2" stays in the same tile. When the player reaches the end, the "Congrats!" message is displayed and the game exits.

Rachel began implementing the stats and characteristics of the player and monsters. It was randomized so that the experience was different every time the player plays the game. She was also responsible for creating the event of the battle and the battle functions (such as, attack, defend and escape). She was unable to complete this portion because of the complexity of her program for the randomized stats and characteristics. However, her program is a standalone which allows her to use this for future games.

Patrick implemented the randomized generation of monsters on the board. The number of monsters ranged from 0 to 5 monsters. The monsters only generated on valid paths ("1"). However, the player counts the monster as a valid path and can move through them.

##### Second Iteration

As a team, we decided to scrap the plan of including monsters and a battle system. Now, it is only a maze game. We decided to hard-code in several boards and let the program randomly select one when the user starts the game.