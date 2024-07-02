For the third exercise of INDA, you will practice modeling behaviors and interactions in Java. You will develop a simple game that involves a player, scoring mechanism, and enemy encounters.

The game works as such:

1. A `Player` and an `Enemy` are initialized with a specific amount of health points (`hp`).
2. The `Player` can move in the game world. Each step costs a specific amount of hp.
3. When a `Player` encounters an `Enemy`, a simple combat occurs reducing `Player`'s hp depending on `Enemy`'s strength.
4. `Player`'s score increases every time they move or defeat an `Enemy`.
5. The game ends when the `Player` runs out of `hp`.

Design and implement classes for the `Player` and `Enemy`. Also, create a `Game` class that oversees the player's actions, score calculation, and end conditions of the game.