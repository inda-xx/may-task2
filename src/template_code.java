```java
public class Player {

    private String name;
    private int score;
    private Point position;

    public Player(String name, Point position) {
        // constructor implementation here
    }

    // getters and setters here

    public void move(int dx, int dy) {
        // implementation here
    }

    public void interactWith(Enemy enemy) {
        // implementation here
    }
}

public class Enemy {

    private String name;
    private int value;
    private Point position;

    public Enemy(String name, int value, Point position) {
        // constructor implementation here
    }

    // getters and setters here
}

public class Point {

    private int x;
    private int y;

    public Point(int x, int y) {
        // constructor implementation here
    }

    // getters and setters here
}

public class Game {

    private Player player;
    private Enemy enemy;

    public Game(Player player, Enemy enemy) {
        // constructor implementation here
    }

    public void play() {
        // implementation here
    }

    public static void main(String[] args) {
        // test game play here
    }
}
```