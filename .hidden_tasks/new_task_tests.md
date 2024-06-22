Create a main method in which you will define two Indamons and make them interact according to the methods you just implemented. Here are some use cases:

1. Create two Indamons with specific initial stats:
```java
Indamon inda1 = new Indamon("Firamon", 100, 20, 10, true);
Indamon inda2 = new Indamon("Aquamonth", 80, 25, 5, true);
```

2. Print information about each Indamon:
```java
inda1.printInfo();
inda2.printInfo();
```

3. Have inda1 attack inda2 and print their stats again after the attack:
```java
inda1.attack(inda2);
inda1.printInfo();
inda2.printInfo();
```