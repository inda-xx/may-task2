## Theme
For the current exercise of INDA, we will continue practicing modeling objects in Java and introduce interaction between these objects. This exercise will introduce you to the building blocks of a simple game application.
 
## 💀 Deadline
This work should be completed before the exercise on **Friday, 23rd September**.

## Task Description

Create a `GameApp` class with three classes: `Player`, `Score`, and `Enemy`. A game consists of one player, zero to many enemies, and scoring which works as follows:

- Each player has a name, an x and y coordinate representing the player's position on a 2D grid, a score object, and a health attribute.
- Each enemy also has an x and y coordinate.
- A player can move one step in either direction (up, down, left, or right) at a time on the grid, adjusting either `x` or `y` by one.
- The Score object tracks points and should have an `addPoints` method. It starts at zero and increments by 100 points each time the player moves.
- Add a `collision` method to the Player class. Its argument should be an Enemy object. If the player and the enemy are at the same position on the grid, the player’s health decreases by one, and the method should return `true`. If no collision occurs, it should return `false`.
- The initial health of the player is three. If the health drops to zero, the player should "die", and the game is over. A `isAlive` method should confirm if the player is alive.