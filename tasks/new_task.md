# Programming Task: Modeling a Bank Account in Java

## Introduction

In this task, you will model a simple bank account object in Java. You will practice creating classes, defining attributes, and implementing methods. This exercise will help you understand the principles of object-oriented programming, and how to structure your code effectively.

## Learning Objectives

By the end of this task, you should be able to:

1. Design and implement classes in Java.
2. Define and use attributes (fields) and methods (functions).
3. Implement constructors and destructors (if applicable).
4. Apply principles of encapsulation, inheritance, and polymorphism.
5. Write unit tests to verify the correctness of your code.

## Task Requirements

### Part 1: Define a Class

1. Create a class named `BankAccount` with the following attributes:
   - `accountNumber` (String): The unique identification number for the bank account.
   - `accountHolder` (String): The name of the account owner.
   - `balance` (double): The current amount of money in the bank account.

2. Implement a constructor to initialize these attributes.

### Part 2: Implement Methods

1. Add getter and setter methods for each attribute.
2. Implement a method named `deposit` to increase the balance by a certain amount and a method named `withdraw` to decrease the balance by a certain amount. Ensure that the withdrawal does not exceed the current balance.
3. Implement a method named `printAccountDetails` that prints all the information about this bank account, including the account number, account holder's name, and current balance.

### Part 3: Unit Testing

1. Write unit tests to verify the correctness of your class implementation.
2. Ensure that all methods are tested, including edge cases (e.g., attempting to withdraw more money than the current balance).

### Part 4: Documentation

1. Add comments and docstrings to your code to explain the purpose of each class, method, and attribute.
2. Ensure that your code adheres to the style guidelines for Java.

## Submission

1. Submit your code by pushing it to your GitHub repository in the `BankAccount` folder.
2. Ensure that all unit tests pass before submission.
3. The grading will be based on the correctness, code style, efficiency, and documentation.

Requirements: {'difficulty': 'medium', 'language': 'Java'}