## Player 

In the `src` folder, create a new class called `Player.java`. The `Player` class should have:

- `String` name  
- `int` hp
- `int` score

Include all necessary getters, setters, and constructors for these fields.

## Enemy 

Create a new class called `Enemy.java`. The `Enemy` class should have:

- `String` name
- `int` strength

Include all necessary getters, setters, and constructors for these fields.

## Game 

Create a new class called `Game.java`. The `Game` class should have:

- `Player` player
- `Enemy` enemy
- `int` gameWorldSize
- `int` playerPosition

It should also have a method for performing actions such as `move()`, `encounterEnemy()`, `calculateScore()`, `isGameOver()`. When designing these methods, consider the return types, parameters, and how they affect the constructed classes.