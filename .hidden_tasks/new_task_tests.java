In this assignment, you will be constructing a basic game using the Java programming language. You will need to create two classes: `Player` and `Enemy`. The game includes the following functionalities: player movement, scoring system, and enemy interactions.

## Player
A `Player` object has the following properties:

- `String name`
- `int score`
- `int xPosition`
- `int yPosition`

The `Player` class should also have:

- A constructor method that takes name, xPosition, and yPosition as parameters and sets score to zero.
- Getters and Setters for all the attributes.
- `move(int x, int y)`: a method that takes new x and y values and updates the player’s position.
- `increaseScore(int increment)`: a method that increases the player's score.

## Enemy
An `Enemy` object has the following properties:

- `String type`
- `int xPosition`
- `int yPosition`

The `Enemy` class also needs:

- A constructor method that takes type, xPosition, and yPosition as parameters.
- Getters and Setters for all the attributes.
- `collide(Player player)`: a method that takes a player object as a parameter and returns true if the player's and enemy's positions coincide. If they collide, the player's score should decrease by 5 points.   

## Main
In the Main class, you will create a `Player` object and a number of `Enemy` objects. You will simulate the player's movement and the encounters with the enemies and print the player's score in the console. The score cannot be less than 0. Also, print a message in the console when a crash with an enemy happens.

# Template

```java
class Player {
    // Define properties here

    // Constructor

    // Getters and Setters

    // move method

    // increaseScore method
}

class Enemy {
    // Define properties here

    // Constructor

    // Getters and Setters

    // collide method
}

class Main {
    public static void main(String[] args) {
        // Your code here
    }
}
```

# Tests
In the tests file, you will create a new Player object and a couple of Enemy objects. Test that the getters and setters work correctly, the score increases when the method increaseScore is called with an integer parameter. Also confirm that if the player and enemy have the same position, the collide method should decrease the player's score by 5 points.

# Solution
This section should contain the solution code.

# Existing Tests
```java 
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class GameTest {
    private Player player;
    private Enemy enemy1;
    private Enemy enemy2;

    @Before
    public void setUp() {
        player = new Player("Player1", 10, 10);
        enemy1 = new Enemy("Enemy1", 5, 5);
        enemy2 = new Enemy("Enemy2", 10, 10); // This enemy is initially at the same position as the player
    }

    // Add tests here
}
``