In this task, you will be creating a simple game of dodging enemy objects while collecting score tablets. The game consists of a player, enemies and score tablets, all represented by objects in the program. The program will consist of several classes - `Player`, `Enemy`, `ScoreTablet`, and `Game`.

The `Player` class will model a player with a String `name`, `int` health, and `int` score. 

The `Enemy` class will model an enemy with `int` damage. 

The `ScoreTablet` class will model a score tablet with `int` addScore. 

The `Game` class will have a `Player` object, an array of `Enemy` objects, and an array of `ScoreTablet` objects. It will also have a method `startGame()`, which contains the game loop. In each iteration of the game loop, an enemy and a score tablet object are randomly selected. If a player collides with an enemy object, the player's health is decreased by the enemy's damage, and if a player collides with a score tablet object, the player's score gets increased by addScore of ScoreTablet. The game continues until the player's health reaches zero.

For the purpose of this task, collision is determined by `boolean` methods `playerEnemyCollision()` and `playerTabletCollision()`. To keep it simple, these methods return a randomly generated boolean value.

At the end of the game, the player's score is printed.

No user interaction is required for this task. The game movement and interactions are automatic and determined by the methods mentioned above.