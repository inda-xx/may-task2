In this exercise, you will create a simple game called "Whack a Mole". The game has a player, a scoring system, and moles (the enemies).

### Task Description

The game works as follows:
- The game board is a 5 by 5 grid.
- The player can whack a spot in the grid by choosing a row and a column.
- Sometimes, there is a mole in that spot. Whacking a mole scores a point.
- The game ends when the player has whacked three moles.

The game should keep track of the score and the remaining number of moles.

Your task is to model the game in Java. You should create ```WhackAMole``` class.

#### Task Requirements

1. Grey out all the spots in the grid.
2. For every turn of the game:
   - A mole randomly appears in a spot in the grid.
   - The player whacks a spot in the grid.
   - If the player's choice is where the mole is, increment the score and decrease the number of moles.
3. The game ends when the player has whacked three moles.
4. Print out the final score and grid, replacing whacked moles with "W".

Your implementation should include the following:

##### Fields

- `int score`
- `int molesLeft`
- `int[][] moleGrid`

##### Methods

- `WhackAMole()`: Constructor for the game. Initializes the score, molesLeft, and moleGrid.
- `void place()`: Places a mole randomly in the grid.
- `void whack(int x, int y)`: Takes a whack at the specified location in the grid.
- `void printGrid()`: Prints the grid without showing where the moles are. Use "*" to represent a spot in the grid and "W" to represent a whacked mole.
- `void printGridToUser()`: Prints the grid showing where the moles are and where the whacked moles were. Use "M" to represent a mole, "*" to represent a spot in the grid, and "W" to represent a whacked mole.