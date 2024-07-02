This is a tentative solution, the actual solution may have slight variations.

```java
public class GameApp {
    public static void main(String[] args) {
        Hero hero = new Hero("Warrior", 15, 10);
        Enemy enemy = new Enemy("Zombie", 8, 5);
        hero.fight(enemy);
        System.out.println(hero.getScore());
        hero.printStats();
    }
}

class Hero {
    String name;
    int hp;
    int attack;
    int score = 0;
    boolean isAlive;

    Hero(String name, int hp, int attack) {
        this.name = name;
        this.hp = hp;
        this.attack = attack;
        this.isAlive = true;
    }

    // Getters...
    // Setters where necessary..

    void fight(Enemy enemy) {
        enemy.hp -= this.attack;
        if (enemy.hp <= 0) {
            enemy.isAlive = false;
            scorePoint();
            System.out.println("Enemy defeated!");
        }
    }

    void scorePoint() {
        this.score++;
    }
    
    void printStats(){
        // print all necessary stats.
    }
    // Other necessary methods...
}

class Enemy {
    String name;
    int hp;
    int attack;
    boolean isAlive;

    Enemy(String name, int hp, int attack) {
        this.name = name;
        this.hp = hp;
        this.attack = attack;
        this.isAlive = true;
    }

    // Getters...
    // Setters where necessary...
    // Other necessary methods...
}
```

**Please remember:** This block is not exhaustive, and additional tests will be performed for complete verification. 

Well designed and robust code is always appreciated.