Please note: The below solution is a basic approach to the task. There are limitless ways to implement a game in Java depending on its complexity and the developer's design. 

```java
public class Game {
  int playerPosition;
  int enemyPosition;
  int score = 0;
  
  public Game() {
    playerPosition = 0;
    enemyPosition = 10;
  }
   
  void movePlayer(int newPosition) {
    playerPosition = newPosition;
  }
  
  void updateScore(int scoreIncrement) {
    score += scoreIncrement;
  }
  
  void interactWithEnemy() {
    if (playerPosition == enemyPosition) {
      updateScore(1);
      enemyPosition = (int) (Math.random() * 20); // new enemy position between 0 and 20
    }
  }
  
  public static void main(String[] args) {
    Game gameObj = new Game();

    gameObj.movePlayer(10);
    gameObj.interactWithEnemy();
  }
}
```
In the above solution, the game consists of the player and an enemy in a 1-dimensional space. Enemy's position is randomly reset when the player encounters them. Player encounters with enemies increase the score by 1.