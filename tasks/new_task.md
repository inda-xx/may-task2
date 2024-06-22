You are to model a mythical creature called "Indamon" at the Campus of the Royal Institute of Technology in Stockholm, Sweden using Java.

Start by creating a class named "Indamon". You are to represent the features of Indamon using the following fields:
  - name (of type String)
  - hp (hit points, of type int)
  - strength (of type int)
  - defense (of type int)
  - isAlive (of type boolean)

Next, encapsulate the fields of Indamon by defining them as private and provide a getter and setter for each of the fields.

Then, implement a constructor for the class that initializes the fields of an Indamon object.

You are to implement another method, "printInfo()", which outputs all the data about an Indamon to the console.

Finally, model a fight between Indamons by writing a method called "attack" that takes in another Indamon object to represent the opponent. The method should reduce the opponent's hp by the amount of strength the attacking Indamon has. The attack method should utilize a formula for the damage done, which is the strength of the attacking Indamon minus the defense of the opponent Indamon.