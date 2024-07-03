## Theme
For the third exercise of INDA, you will practice building a simple game application in Java. The game should consist of player movement control, a scoring system, and interactions with enemy characters.

## 💀 Deadline
This assignment should be completed before the exercise on **Friday, 30th September**.

## 👩‍🏫 Instructions
For instructions on how to complete and submit the assignment, please refer to the [assignments section of the course instructions](https://gits-15.sys.kth.se/inda-22/course-instructions#assignments).

## 📝 Preparation
You must read and answer the questions in the OLI material for Module 3.

- Read [Simple Games with User Interaction](https://kth.oli.cmu.edu/jcourse/webui/syllabus/module.do?context=f5e5a808ac1f088812f2a8ce315bac60)
- If you have not done so, go to [OLI](https://kth.oli.cmu.edu/), sign up, and register for the course key `dd1337-ht22`.

## ✅ Learning Goals
After this week, you should be familiar with:
- Basic Java Input/Output
- Player movement control
- Building a simple scoring system
- Interactions between player and Non-playable characters (NPCs)

## 🎮 Assignment
You are tasked to create a text-based console game. The player controls a character that can move in four directions: up, down, left and right within a game field. The game field is two-dimensional and of size 10x10.

In the game field, there are items that the player can pick up by moving the character to the location of the item. Each item contributes points to the player's score. 

There are also enemies in the game field. If the player's character reaches an enemy's position, the game ends, and the player's final score is displayed.

Your task is to implement the game application. You should carefully consider how to design your classes to model the player, the items, and the enemies. 

## Methods to be implemented:

### Class Player:

- `public void move(String direction)`: This method takes a string representing the direction to move in (up, down, left, right) and moves the player character in that direction by one step. You must make sure that the character does not go out of the game field (out of boundary checks).

- `public void pick_up(Item item)`: This method takes an Item object and adds the points from the item to the player's score. You can assume that this function will only be called when the player character is on the same position as an item.

### Class Item:

- `public int getPoints()`: This method returns the number of points the item is worth.

### Class Enemy:

- `public void move()`: This method moves the enemy in a random direction (up, down, left, or right) by one step. You must make sure that the enemy does not go out of the game field (out of boundary checks).