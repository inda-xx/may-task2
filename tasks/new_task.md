For the second exercise of INDA, you will practice building interactive game components in Java. In your game, you will have a hero who must fight enemies and earn points.

## Deadline
 The task must be completed before the exercise on **Friday, 16th September**.

## Instructions
For instructions on how to complete and submit the assignment, please refer to the [assignments section of the course instructions](https://gits-15.sys.kth.se/inda-22/course-instructions#assignments).

## Preparation
You must read and answer the questions in the OLI material for Module 2.

- Read [Game Development Basics](content-link)
- If you have not done so, go to [OLI](https://kth.oli.cmu.edu/), sign up, and register for the course key `dd1337-ht22`.

The Learning Goals this week include:
-   
- Designing Java classes for game characters (Hero and Enemy)
- Adding class methods for creating character and enemy interactions
- Using the `main` method to run the game
- Implementing game scoring system
- Error handling for game events

## Assignment
In the [`src`](src) folder, create a new class `GameApp.java`. Your game must contain:

- Hero Class with:
    - `String` name  
    - `int` hp (**hit points**)
    - `int` attack 
    - `boolean` isAlive

- Enemy Class with:
    - `String` name  
    - `int` hp (**hit points**)
    - `int` attack 
    - `boolean` isAlive

- Class methods should include:
    - *fight()*: This will be a method in the Hero class, where the hero fights a given enemy. The damage done follows a similar formula to the existing code. It should print the status to the terminal.
    - *scorePoint()*: A method in the Hero class where the hero earns points when an enemy is defeated.
    - Both classes should have getters for all attributes and setters wherever necessary.
    - A *printStats()* method for the hero to print all current game statistics.

- For simplicity, all characters will have static attributes except for isAlive which is initially set to true and becomes false when hp <= 0.