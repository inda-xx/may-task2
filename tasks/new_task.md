# Task

In this programming task, you are required to write a program in Java to solve a medium level problem.

## Problem

You need to create a `MessageEncoder` Java class for the following task.

A secret message is embedded in a text and we need to decode it. The message is marked with numbers between the range of 1 and 50 inclusive and the marks are ending with a '#'. The marks and their corresponding letters are transformed with each other (i.e. 1 means 'a', 2 means 'b', ... 50 means 'y', '#0' means 'z').

Your `MessageEncoder` class should have the following methods:

- `public MessageEncoder(String text)`: This constructor should preload the text to be processed.
- `public String decode()`: This method should return the decoded message by replacing numbers ended with '#' with their corresponding letters.


### Input

- The input text only contains numbers('0'-'9'), '#' characters, and english small letters('a'-'z').

### Output

- The decode function should return a String, the decoded message.

## Example

```java
MessageEncoder encoder = new MessageEncoder("1#2#3#50#0#b#c");
System.out.println(encoder.decode());
```

Output: 
```java
"abcyzbc"
```

## Constraints

- The input string length won't exceed 10^3.

# Testing

The solution should pass the following test case:

- The MessageEncoder constructor is given the string "25#50#1#c#20#31#10#0#7#7#". Processing this string with decode() should return "yaycotjzzhh".

Your solution will be graded on:

- Correctness
- Code style
- Use of Java idioms