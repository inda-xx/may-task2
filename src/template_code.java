Create a new class called `Game.java`. The `Game` class should have:

- two objects - `Player` and `Enemy` as instance variables.       
- a `set` and `get` method for each instance variable  
- a constructor for initiating the `Player` and `Enemy` objects.
- a method, `startGame` which prints the state of the `Player` and `Enemy` and then calls the `attack` method of the `Player`

Create a new class called `Player.java`. The `Player` class should have:

- a `String name`  
- an `int` hitpoints (hp) 
- a `boolean` fainted
- a constructor for initiating the fields.
- a `set` and `get` method for each field.
- an `attack` method that calls the `hit` method of the `Enemy` object

Create a new class called `Enemy.java`. The `Enemy` class should have:

- a `String name`  
- an `int` hitpoints (hp) 
- a `boolean` fainted
- a constructor for initiating the fields.
- a `set` and `get` method for each field.
- a `hit` method that decreases the hp by 1 and sets `fainted` to `true` if `hp` becomes `0`