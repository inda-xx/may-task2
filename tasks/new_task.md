In this programming task, you will implement the simplified version of a game application using Java. The game involves two roles: player and enemy. The player is able to score points by interacting with the enemy. The player is also able to move across a simple 2-dimensional grid. This task consists of implementing four classes:

1. `Player` class
2. `Enemy` class
3. `Game` class
4. `Point` class

#### Player class
Create a Player class which encapsulates the details of the Player. The Player class should have the following fields:
- `name (String)`
- `score (int)`
- `position (Point)`

It should also have the following methods:
- A constructor that sets `name` and `position`
- Getters and setters for all fields
- `move(int dx, int dy)`: to move the player by `dx` and `dy` in the 2-dimensional grid.
- `interactWith(Enemy enemy)`: to interact with an `enemy`, adding the enemy's value to the player's score.

#### Enemy class
Create an Enemy class which encapsulates the details of the Enemy. The Enemy class should have the following fields:
- `name (String)`
- `value (int)`
- `position (Point)`

It should also have the following methods:
- A constructor that sets `name`, `value`, and `position`
- Getters and setters for all fields

#### Point class
Create a Point class which encapsulates details of a position in a 2-dimensional grid. The Point class should have the following fields:
- `x (int)`
- `y (int)`

It should also have the following methods:
- A constructor that sets `x` and `y`
- Getters and setters for all fields

#### Game class
Create a Game class which encapsulates details of the game and controls the game flow. The Game class should have the following fields:
- `player (Player)`
- `enemy (Enemy)`

It should also have the following methods:
- A constructor that sets `player` and `enemy`
- `play()`: to start the game, making the player interact with the enemy if they have the same position.

Ensure the `main` function in `Game.java` can compile the code, and running it gives the correct behaviour as stated above.