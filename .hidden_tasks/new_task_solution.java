```java
public class Indamon {
    // your previous code here

    private int score = 0;
    private int x = 0;
    private int y = 0;

    public void move(int x, int y) {
        this.x = x;
        this.y = y;
        this.score++;
    }

    public int getScore() {
        return this.score;
    }

    public Integer[] getPosition(){
        return new Integer[]{this.x, this.y};
    }
}

public class Enemy {
    private String name;
    private int hp;
    private int attack;
    private int defense;
    private int x = 0;
    private int y = 0;

    public Enemy(String name, int hp, int attack, int defense) {
        this.name = name;
        this.hp = hp;
        this.attack = attack;
        this.defense = defense;
    }

    public int getAttack(){
        return this.attack;
    }

    public void move(int x, int y){
        this.x = x;
        this.y = y;
    }

    public Integer[] getPosition(){
        return new Integer[]{this.x, this.y};
    }
}
```