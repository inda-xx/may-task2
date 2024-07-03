the world of text-based games, your task is to create a simple Java game application called "Indamon Battle". In this game, players will battle against each other using their Indamon and score points accordingly.

Your primary task includes following functionalities:
1. `Player Movement`- For this, you can use the concept of current `Position` and method to `Move` to a new position in the game world.
2. `Scoring System`- A simple scoring system based on the outcome of the battles.
3. `Enemy Interactions`- The core of the game; each player will attack their enemy until one's health point reaches zero.

## Requirements:

1. **Difficulty:** Medium
2. **Language:** Java

Below is the existing code which models the concept of `Indamon`. You can use this code as a starting point.

## Template

```java
class Player {
    private String name;
    private int score;
    private int position;
    private Indamon indamon;

    // Constructor
    public Player(String name, Indamon indamon) {
        this.name = name;
        this.indamon = indamon;
        this.score = 0;
        this.position = 0;
    }

    // Getter methods
    // TODO: Implement getter methods

    // Setter methods
    // TODO: implement setter methods

    // Player movement method
    // TODO: Implement move method

    // Battle method
    // TODO: implement battle method, where this player battles another player.

    // Print player info method
    // TODO: Implement printPlayerInfo method

    // main method
    public static void main(String[] args) {
        // TODO: Implement main method
    }
}
```
## Tests

You will need to create tests to ensure your classes for Player, Indamon, and the interaction between them are working as expected. Here are some possible test methods you may want to include, though yours may vary based on your implementation. 

```java
testGetName(), testGetScore(), testGetPosition(), testGetIndamon()
testSetName(), testSetScore(), testSetPosition(), testSetIndamon()
testMove(), testBattle()
```

## Solution

This will be dependent on your specific implementation of the task; multiple solutions may be possible. However, you should at least have implemented all the required elements of the task in a manner that adheres to good coding conventions and practices, and all your tests should pass. 

Your main method should demonstrate the creation of two Player objects, the ability to move Players around the game world, and a battle between two Players that results in a change to their scores.

Remember, a strong solution includes detailed comments explaining your code, especially any parts that may be difficult to understand, and is well-organized, with related methods grouped together.

## Here is the existing code to take inspiration from:

```java
class Indamon {
    // existing code
}
```

In the test class for the solution, make sure to have all test methods for each functionality of the application; for instance, player movements, scoring system, and enemy interactions. 

## Existing Tests

```java
class IndamonTest {
    // existing tests
}
``