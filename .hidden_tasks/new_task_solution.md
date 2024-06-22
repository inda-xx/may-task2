```java
public class Indamon {
  private String name;
  private int hp;
  private int strength;
  private int defense;
  private boolean isAlive;

  public Indamon(String name, int hp, int strength, int defense, boolean isAlive) {
    this.name = name;
    this.hp = hp;
    this.strength = strength;
    this.defense = defense;
    this.isAlive = isAlive;
  }

  public void printInfo() {
    System.out.println("Name: " + name);
    System.out.println("HP: " + hp);
    System.out.println("Strength: " + strength);
    System.out.println("Defense: " + defense);
    System.out.println("Is Alive: " + isAlive);
    System.out.println();
  }

  public void attack(Indamon opponent) {
    int damage = this.strength - opponent.defense;
    opponent.hp -= damage;
    if(opponent.hp <= 0) {
        opponent.isAlive = false;
        System.out.println(this.name + " defeated " + opponent.name + "!");
    }
  }

  // Getters and Setters omitted for brevity

  public static void main(String[] args) {
    Indamon inda1 = new Indamon("Firamon", 100, 20, 10, true);
    Indamon inda2 = new Indamon("Aquamonth", 80, 25, 5, true);

    inda1.printInfo();
    inda2.printInfo();
    inda1.attack(inda2);
    inda1.printInfo();
    inda2.printInfo();
  }
}
```