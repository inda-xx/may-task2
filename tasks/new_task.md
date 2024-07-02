For this exercise, you will develop a simple Java game that allows a player to move around a 2D grid, gather points by collecting items, and avoid enemies who can end the game. The game ends when the player collects all items or encounters an enemy.

Three Java classes need to be implemented: `Player`, `Item`, and `Enemy`.

1. `Player` class: Should have `int x` and `int y` as instance variables representing the player's location on a 2D grid. It should also have a `score` instance variable. The player starts at position (0, 0) with a score of 0.

2. `Item` class: Should have `int x` and `int y` as instance variables representing the item's location on a 2D grid. Also, an `int pointsValue` variable, holding the points the player can achieve by collecting this item.

3. `Enemy` class: Should have `int x` and `int y` as instance variables representing the enemy's location on a 2D grid.

All three classes should have a method `move()` to change their position on the grid. The `Player` has an additional method, `collect(Item item)`, which adds the item's points value to the player's score and removes the item from the game. If the player is in the same location as an enemy, the game ends.

The specific function signatures will be provided in the Template section.