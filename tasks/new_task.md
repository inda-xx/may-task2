**The Return of Indamon**

In this exercise, you will build a simple virtual game based on the legendary Indamons fighting. The game will include player's movement, a scoring system to calculate points based on the battle outcome, and interactions with enemy players. You will also improve the `attack` method of your `Indamon` class. 

You will be creating a `Game` Class that controls the fighting between two players. The `Game` class will have the following attributes:
- `Player1`: An instance of `Indamon` representing Player 1.
- `Player2`: An instance of `Indamon` representing Player 2.
- `Player1Score`: An integer tracking Player 1's score.
- `Player2Score`: An integer tracking Player 2's score.

The `Game` class will have the following methods:
- `playRound()`: Causes Player 1 to "attack" Player 2 and then Player 2 to "attack" Player 1. If player 'i' faints, increment the score of player 'j' by 1 and revive the fainted player.
- `getPlayer1Score()`: Returns the score of Player 1.
- `getPlayer2Score()`: Returns the score of Player 2.

The 'attack' method in 'Indamon' class should be improved to incorporate scoring. The method should return an integer. If the enemy is defeated (Enemy's hit points become zero or less), the method should return 1, else it should return 0.

The exercise will be graded based on the correct implementation of the `Game` and modification of the `attack` method in `Indamon` class and how well it interacts with the `Game` class.