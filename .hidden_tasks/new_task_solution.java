```java
class Player {
    private int x, y, score;

    public Player() {
        this.x = 0;
        this.y = 0;
        this.score = 0;
    }

    public void move(int newX, int newY) {
        this.x = newX;
        this.y = newY;
    }

    public void collect(Item item) {
        if (this.x == item.getX() && this.y == item.getY()) {
            this.score += item.getPointsValue();
            // Remove item from game
        }
    }
}

class Item {
    private int x, y, pointsValue;

    public Item(int x, int y, int pointsValue) {
        this.x = x;
        this.y = y;
        this.pointsValue = pointsValue;
    }

    public void move(int newX, int newY) {
        this.x = newX;
        this.y = newY;
    }

    public int getPointsValue() {
        return this.pointsValue;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}

class Enemy {
    private int x, y;

    public Enemy(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void move(int newX, int newY) {
        this.x = newX;
        this.y = newY;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}

class Game {
    public static void main(String[] args) {
        Player player = new Player();
        Item item = new Item(1, 1, 100);
        Enemy enemy = new Enemy(2, 2);

        player.move(1,1);
        player.collect(item);

        // Test if item is collected and score increased..
        
        player.move(2,2);

        // Test if game ends after meeting enemy..
    }
}
```