# Plan

- [Plan](#plan)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Lesson 1: Getting Started with Python](#lesson-1-getting-started-with-python)
  - [Lesson 2: Variables and Basic Data Types](#lesson-2-variables-and-basic-data-types)
  - [Lesson 3: Conditional Statements](#lesson-3-conditional-statements)
  - [Lesson 4: Loops and Simple Games](#lesson-4-loops-and-simple-games)
  - [Lesson 5: Functions](#lesson-5-functions)
  - [Lesson 6: Lists and Loops](#lesson-6-lists-and-loops)
  - [Lesson 7: Dictionaries](#lesson-7-dictionaries)
  - [Lesson 8: Strings and String Manipulation](#lesson-8-strings-and-string-manipulation)
  - [Lesson 9: File Handling](#lesson-9-file-handling)
  - [Lesson 10: Error Handling](#lesson-10-error-handling)
  - [Lesson 11: Classes and Objects (Intro to OOP)](#lesson-11-classes-and-objects-intro-to-oop)
  - [Lesson 12: Modules and Importing](#lesson-12-modules-and-importing)
  - [Lesson 13: Recap and Mini-Project](#lesson-13-recap-and-mini-project)

## Setting Up the Environment

1. Install Python
   - Download the latest Python version from python.org. Ensure you
     check the option to “Add Python to PATH” during installation.
2. Code Editor/IDE:
   - Use Visual Studio Code (VS Code): It’s beginner-friendly and highly
     customizable.
   - Alternatively, use an IDE like PyCharm Community Edition for an
     all-in-one Python environment.
3. Useful Extensions for VS Code:
   - Python extension by Microsoft.
   - Code Runner for quick execution.
   - Jupyter (optional, if you’d like to explore notebooks later).
4. Command Prompt Basics:
   - Teach basic navigation (cd, dir) and how to run Python scripts
     (python filename.py).
5. Install Additional Tools:
   - Thonny: A simple Python IDE great for beginners, particularly kids.
   - Optionally, set up a virtual environment for projects:
     - `python -m venv env`.

## Lesson 1: Getting Started with Python

- Objective: Write and run your first Python program.
- Topics:
  1. What is Python, and why use it? (Keep it light and relatable).
  2. Writing your first Python script: print("Hello, World!").
  3. How to run Python scripts (in the IDE or terminal).
  4. Explore the `REPL` (interactive mode): Try simple commands like `1 + 1`,
     `"Hello".upper()`.

- [Activity](lessons/01.py): Customize the “Hello, World!” program to
  greet with his name or favorite phrase.

## Lesson 2: Variables and Basic Data Types

- Objective: Learn how to store and manipulate data.

- Topics:
  1. Variables: Assign and reassign (`name = "John"`, `age = 12`).
  2. Data types: Strings, integers, floats, booleans.
  3. Simple input/output: `input()` and `print()`.
  4. Basic math operations (`+`, `-`, `*`, `/`, `%`).

- [Activity](lessons/02.py): Write a program that calculates the number
  of days until his next birthday.

## Lesson 3: Conditional Statements

- Objective: Make decisions in programs.

- Topics:
  1. `if`, `elif`, `else` statements.
  2. Comparison operators (`>`, `<`, `==`, `!=`, etc.).
  3. Logical operators (`and`, `or`, `not`).

- [Activity](lessons/03.py): Write a program that checks if a number is
  odd or even.

## Lesson 4: Loops and Simple Games

- Objective: Introduce loops to automate repetitive tasks.

- Topics:
  1. for loops with ranges.
  2. while loops and their conditions.
  3. Breaking out of loops.

- [Activity](lessons/04.py): Create a simple guessing game where the
  computer picks a random number, and the user has to guess it.

## Lesson 5: Functions

- Objective: Understand how to group code into reusable functions.
- Topics:
  1. Defining functions with def.
  2. Function arguments and return values.
  3. Scope of variables (local vs. global).
- [Activity](lessons/05.py): Write a function that converts temperatures
  between Celsius and Fahrenheit.

## Lesson 6: Lists and Loops

- Objective: Work with collections of data using lists and loops.
- Topics:
  1. Creating and modifying lists (append, remove, slicing).
  2. Iterating over lists with for loops.
  3. Common list operations (len, in, index).
- [Activity](lessons/06.py): Create a program that takes a list of
  numbers and calculates the average.

## Lesson 7: Dictionaries

- Objective: Use dictionaries to store and retrieve data by key-value
  pairs.
- Topics:
  1. Creating dictionaries.
  2. Accessing, adding, and updating values.
  3. Iterating over dictionaries (keys, values, items).
- [Activity](lessons/07.py): Write a program that tracks favorite foods
  for different people using a dictionary.

## Lesson 8: Strings and String Manipulation

- Objective: Explore Python’s powerful string-handling capabilities.
- Topics:
  1. String methods (split, join, replace, strip).
  2. Formatting strings (f-strings, .format).
  3. Escape sequences (e.g., \n, \t).
- [Activity](lessons/08.py): Write a program that formats and prints a
  “mad lib” story based on user input.

## Lesson 9: File Handling

- Objective: Learn how to read from and write to files.
- Topics:
1. Opening files in different modes (r, w, a).
2. Reading file contents (read, readlines).
3. Writing to files.
- [Activity](lessons/09.py): Create a program that saves user input
  (e.g., a diary entry) to a text file and reads it back.

## Lesson 10: Error Handling

- Objective: Write robust programs by managing errors gracefully.
- Topics:
  1. Using try, except, and finally.
  2. Handling specific exceptions (e.g., ValueError).
  3. Raising exceptions with raise.
- [Activity](lessons/10.py): Create a program that asks for numbers,
  handles invalid input gracefully, and calculates their sum.

## Lesson 11: Classes and Objects (Intro to OOP)

- Objective: Introduce basic object-oriented programming concepts.
- Topics:
  1. Defining a class and creating objects.
  2. Class attributes and methods.
  3. __init__ method for initialization.
- [Activity](lessons/11.py): Write a class for a “Pet” with attributes
  like name and species, and a method to display a greeting (e.g.,
  “Woof! My name is Max!”).

## Lesson 12: Modules and Importing

- Objective: Use Python’s modularity to organize code and use libraries.
- Topics:
  1. Importing built-in modules (e.g., math, random).
  2. Writing your own modules.
  3. Understanding import, from ... import, and as.
- [Activity](lessons/12.py): Use the `random` module to create a simple
  dice-rolling simulation.

## Lesson 13: Recap and Mini-Project

- Objective: Consolidate knowledge and create a small, complete program.
- [Activity](lessons/13.py):
  - Write a text-based adventure game using everything learned
    (functions, loops, conditionals, dictionaries, etc.).
  - Example: A simple “choose your own adventure” story where decisions
    affect the outcome.
