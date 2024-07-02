```java
class Player {
    private int x, y, score;

    public Player() {
        // Implement this
    }

    public void move(int newX, int newY) {
        // Implement this
    }

    public void collect(Item item) {
        // Implement this
    }
}

class Item {
    private int x, y, pointsValue;

    public Item(int x, int y, int pointsValue) {
        // Implement this
    }

    public void move(int newX, int newY) {
        // Implement this
    }
}

class Enemy {
    private int x, y;

    public Enemy(int x, int y) {
        // Implement this
    }

    public void move(int newX, int newY) {
        // Implement this
    }
}

class Game {
    // Here you will add the game's main loop, where you manage player's interactions with items and enemies.
}
```