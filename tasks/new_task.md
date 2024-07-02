Your task for the second exercise of INDA is to create a simple game application. This game application should allow player movement across a 2D grid as well as a scoring system that increases every time a player successfully interacts with an object/enemy on the grid.

## Theme
The theme of this game can be anything but for this task, we will provide a basic setup: You are a reckless treasure hunter searching for the legendary lost Indamon Gold inside a perilous ancient maze filled with dangerous traps and mystical creatures.

## 💀 Deadline
This work should be completed before the exercise on **Friday, 16th September**.

### Exercise 2.0 -- Setting up
Create the following classes:
- `Game.java` - The main class that will start the game
- `Player.java` - Will represent the player character
- `Enemy.java` - Will represent the enemies in the game

And the following enums:
- `Direction.groovy` - Will represent the possible directions of movement (UP, DOWN, LEFT, RIGHT)

### Exercise 2.1 -- Player Class
Your `Player.java` should have the following fields:
- `int x` - The player's x coordinate
- `int y` - The player's y coordinate
- `int score` - The player's score

It should have getters for all fields and setters just for `x`, `y` and `score`. It should also have a `move(Direction direction)` method to move the player along the grid and an `interact(Enemy enemy)` method that increases the player score and removes the enemy from the game.

### Exercise 2.2 -- Enemy Class
Your `Enemy.java` should have the following fields:
- `int x` - The enemy's x coordinate
- `int y` - The enemy's y coordinate

And getters for the fields.

Flesh out these classes with appropriate methods and fields. If you design this system right, you will be well on your way to creating a unique game of your own!

### Exercise 2.3 -- Game Class
The `Game.java` class should have a `start()` method that runs it. It should create and place a player object and several enemy objects within the game world. Then, it should start looping, allowing the player to move in all directions and interact with enemies. The game should run until the player decides to quit or all enemies have been interacted with.

### Tests
Besides the task implementation you should also create test classes to make sure everything is working as expected.

Don't forget to take advantage of the code given as it can be very helpful. You may also use it as a starting point for your code structure. Good luck!