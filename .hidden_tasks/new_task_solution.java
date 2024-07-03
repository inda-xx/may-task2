```java
import java.util.Random;

class Player {
    private String name;
    private int health;
    private int score;
    
    public Player(String name, int health) {
        this.name = name;
        this.health = health;
        this.score = 0;
    }
    
    // getters and setters
}

class Enemy {
    private int damage;
    
    public Enemy(int damage) {
        this.damage = damage;
    }
    
    // getters and setters
}

class ScoreTablet {
    private int addScore;

    public ScoreTablet(int addScore) {
        this.addScore = addScore;
    }

    // getters and setters
}

class Game {
    private Player player;
    private Enemy[] enemies;
    private ScoreTablet[] scoreTablets;
    private Random random;

    public Game(Player player, Enemy[] enemies, ScoreTablet[] scoreTablets) {
        this.player = player;
        this.enemies = enemies;
        this.scoreTablets = scoreTablets;
        this.random = new Random();
    }

    // getters and setters
   

    public void startGame() {
        while(player.getHealth() > 0) {
            if(playerEnemyCollision()) {
                // Get damage of a random enemy
                int damage = enemies[random.nextInt(enemies.length)].getDamage();
                player.setHealth(player.getHealth() - damage);
            }
            
            if(playerTabletCollision()) {
                // Get addScore of a random score tablet
                int addScore = scoreTablets[random.nextInt(scoreTablets.length)].getAddScore();
                player.setScore(player.getScore() + addScore);
            }      
        }
        
        System.out.println(player.getName() + "'s score is: " + player.getScore());
    }
    
    private boolean playerEnemyCollision() {
        // Generate a random boolean
        return random.nextBoolean();
    }
    
    private boolean playerTabletCollision() {
        // Generate a random boolean
        return random.nextBoolean();
    }
}

public class Main {
    public static void main(String[] args) {
        Player player = new Player("Player", 10);
        Enemy[] enemies = {new Enemy(1), new Enemy(2), new Enemy(3)};
        ScoreTablet[] scoreTablets = {new ScoreTablet(1), new ScoreTablet(2), new ScoreTablet(3)};
        Game game = new Game(player, enemies, scoreTablets);
        game.startGame();
    }
}
```