Provide a suggested solution for the task.

### Here is another example:
```java
public class Player {
    private String name;
    private int score;
    private Point position;

    public Player(String name, Point position) {
        this.name = name;
        this.score = 0;
        this.position = position;
    }

    // getters and setters here

    public void move(int dx, int dy) {
        position.setX(position.getX() + dx);
        position.setY(position.getY() + dy);
    }

    public void interactWith(Enemy enemy) {
        if (this.position.getX() == enemy.getPosition().getX() && this.position.getY() == enemy.getPosition().getY())
            this.score += enemy.getValue();
    }
}

public class Enemy {
    private String name;
    private int value;
    private Point position;

    public Enemy(String name, int value, Point position) {
        this.name = name;
        this.value = value;
        this.position = position;
    }

    // getters and setters here
}

public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // getters and setters here
}

public class Game {
    private Player player;
    private Enemy enemy;

    public Game(Player player, Enemy enemy) {
        this.player = player;
        this.enemy = enemy;
    }

    public void play() {
        player.interactWith(enemy);
    }

    public static void main(String[] args) {
        Point playerPosition = new Point(1, 1);
        Point enemyPosition = new Point(1, 1);
        Player player = new Player("Sam", playerPosition);
        Enemy enemy = new Enemy("Zombie", 10, enemyPosition);
        Game game = new Game(player, enemy);
        game.play(); // player and enemy have same position, player gets enemy's value added to score
    }
}
```