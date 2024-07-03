For this task, you are required to implement a simple game application where a player can move around, score points by collecting coins, and interact with enemies. For this implementation, develop three classes: `Player`, `Coin`, and `Enemy`.

### Player Class: 

Player class will have following attributes:
- `String` name
- `int` x (`x`-coordinate)
- `int` y (`y`-coordinate)
- `int` score (initially 0) 

And the following methods:
- `void moveUp(), moveDown(), moveRight(), moveLeft()` to alter the player's x,y coordination.
- `void collect(Coin c)` increases player's score and remove the Coin from the game.
- `void interact(Enemy e)` to interact with enemy. If the enemy is stronger, the game terminates and if the player is stronger, the score increases by 5.

### Coin Class:

Coin class will have following attributes:
- `int` x (`x`-coordinate)
- `int` y (`y`-coordinate)
- `int` value (the value that this coin adds to player's score)

### Enemy Class:

Enemy class will have following attributes:
- `int` x (`x`-coordinate)
- `int` y (`y`-coordinate)
- `int` power 

The player and enemies will exist on a grid. Interactions only happen when they share the same (x,y) coordinates on the grid. Player can collect a coin if it exists on the position where player is located.

### Tests

Create a test suite `GameTest` that includes robust, detailed, edge cases and performance considerations for testing all implemented methods in `Player`, `Coin`, and `Enemy`. 

### Solution

The solution to this task should create instances of the `Player`, `Coin` and `Enemy`, and implement all the necessary methods as outlined in the task description. The application should be able to simulate simple movement and interaction between objects.