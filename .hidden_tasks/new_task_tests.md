## Theme
For the third exercise of INDA, you are tasked with creating a simple game application in Java. This will help you deepen your understanding of object-oriented programming in Java, while also introducing you to the basics of game development.

## Instructions
- The game should have a player that can move in any direction.
- There will be points scattered around the map which the player can collect and add to their score.
- There will also be enemy characters who can interact with the player. Interactions with enemies should decrease the player's score. 
- Implement a method `player.move(Direction direction)` which takes direction as an input and changes the position of the player accordingly.
- Implement a method `player.collect(Point point)` which increments the player's score when a point is collected.
- Implement a method `player.interact(Enemy enemy)` which decreases the player's score when an encounter with an enemy occurs.

### Functionalities to be implemented in respective classes :

#### Player Class
* move(Direction direction)
* collect(Point point)
* interact(Enemy enemy)

#### Point Class
* checkIfCollected(Player player)

#### Enemy Class
* checkInteraction(Player player)

## Tests
1. Test the player's movement in each direction.
2. Test the collection of points and confirm that the score increases.
3. Test the interactions with enemies and confirm it decreases the player's score.

## Solution
```java
class Coordinate {
  int x, y;
  // constructor, getters, setters..
}

enum Direction {
  NORTH, EAST, SOUTH, WEST;
}

class Player {
  Coordinate pos;
  int score;
  public void move(Direction direction) { /* implementation */ }
  public void collect(Point point) { 
    if(point.checkIfCollected(this)){
      this.score++; 
    }
  }
  public void interact(Enemy enemy) {
    if(enemy.checkInteraction(this)){
      this.score--; 
    }
  }
  // constructor, getters, setters..
}

class Point {
  Coordinate pos;
  public boolean checkIfCollected(Player player) { /* implementation */ }
  // constructor, getters, setters..
}

class Enemy {
  Coordinate pos;
  public boolean checkInteraction(Player player) { /* implementation */ }
  // constructor, getters, setters..
}
```

After constructing an object of Player class, call the move, collect and interact methods to see how player's position and score attributes change according to the interaction on the map