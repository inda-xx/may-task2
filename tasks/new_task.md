You are to implement a dragon character named SuperFuzzyFuzzball in the game Dungeons and Dragons. The dragon character shall have the following attributes- Name, Current Health, Maximum Health, Attack, Defense, Magic. Also implement following interactions- "attackEnemy", "castSpell", "rest", "isAlive", and "getInfo".

Implement in Java with medium difficulty.

1) Create a class `SuperFuzzyFuzzball` with the above attributes.
2) Implement the attackEnemy method, which will take another `SuperFuzzyFuzzball` object as an argument that will represent the enemy for the duration of the attack. Damage calculation will be same as in Indamon - `damage = Attack/Defense`
3) Implement the castSpell method, which will consume magic and do magic damage to an enemy SuperFuzzyFuzzball.
4) Implement the rest method, which will recover a defined amount of health points.
5) Implement an isAlive function that reeturns `true` if the character is alive, or `false` if the character is dead.
6) Implement a `getInfo` method that print all the info of a SuperFuzzyFuzzball character.