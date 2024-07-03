```java
@Test
public void testMove() {
    glassey.move(1,1);
    assertEquals(1, glassey.getScore());
}

@Test
public void testEncounterEnemy(){
    Enemy enemy = new Enemy("Enemy1", 10, 4, 5);
    glassey.move(0,0);
    enemy.move(0,0);
    // If Glassey and Enemy1 are at the same location Glassey should have hp 6 as Enemy1's attack value is 4
    assertEquals(6, glassey.getHp());
}
```