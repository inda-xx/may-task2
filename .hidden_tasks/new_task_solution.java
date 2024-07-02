```java
class SuperFuzzyFuzzball {
    private String name;
    private int currentHealth;
    private int maxHealth;
    private int attack;
    private int defense;
    private int magic;
    
    public SuperFuzzyFuzzball(String name, int maxHealth, int attack, int defense, int magic) {
        this.name = name;
        this.maxHealth = maxHealth;
        this.currentHealth = maxHealth; // current health should be equal to maxHealth at the beginning
        this.attack = attack;
        this.defense = defense;
        this.magic = magic;
    }

    // getters and setters
    // Add your code here

    public void attackEnemy(SuperFuzzyFuzzball enemy) {
        int damage = attack / enemy.getDefense();
        enemy.setCurrentHealth(enemy.getCurrentHealth() - damage);
    }

    public void castSpell(SuperFuzzyFuzzball enemy) {
        // Consume magic to cast spell and do magic damage
        // Add your code here
    }

    public void rest() {
        // Recover health points when characters rest
        // Add your code here
    }

    public boolean isAlive() {
        return currentHealth > 0;
    }

    public void getInfo() {
        System.out.println("Name: " + name);
        System.out.println("Current Health: " + currentHealth);
        System.out.println("Max Health: " + maxHealth);
        System.out.println("Attack: " + attack);
        System.out.println("Defense: " + defense);
        System.out.println("Magic: " + magic);
    }
}
```