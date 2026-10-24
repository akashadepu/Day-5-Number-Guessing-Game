# Number Guessing Game --- Day 5

## Project Overview

A beginner-friendly Python command-line game. The program chooses a
random integer from 1 to 100, and the player keeps guessing until they
find it. After each incorrect guess, the program says whether the guess
is too low or too high.

## Objectives

-   Practice `while` loops and conditional statements.
-   Generate a random number using Python's `random` module.
-   Count guesses and stop the loop with `break`.

## Technologies

-   Python 3
-   `random` module (Python standard library)

## Project Structure

``` text
Day5-Number-Guessing-Game/
├── number_guessing_game.py
└── README.md
```

## How to Run

Save the code as `number_guessing_game.py`, open a terminal in that
folder, and run:

``` bash
python number_guessing_game.py
```

On Windows, you can also try `py number_guessing_game.py`.

## Code

``` python
import random

number = random.randint(1,100)
total = 0

print("Guess the number between 1 to 100")

while True:
    user = int(input("Enter your number: "))
    total += 1
    if user == number:
        print(f"Correct! You found the number: {number}")
        print(f"Attempts taken: {total}")
        
        break
    elif user < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

```

## How It Works

1.  `random.randint(1, 100)` selects a secret integer from 1 to 100,
    inclusive.
2.  `attempts` starts at zero.
3.  `while True` keeps asking for guesses.
4.  `attempts += 1` increases the count after every guess.
5.  `if`, `elif`, and `else` tell the player whether the guess is
    correct, too low, or too high.
6.  `break` ends the game when the correct number is guessed.

## Sample Gameplay

Example only; the secret number changes each time the game runs.

``` text
Guess the number between 1 and 100.
Enter your number: 20
Too low! Try again.
Enter your number: 60
Too high! Try again.
Enter your number: 42
Correct! You found the number 42
Attempts taken: 3
```

## Test Cases

  Test                            Expected result
  ------------------------------- ----------------------------------------------------
  Guess below the secret number   Displays "Too low! Try again."
  Guess above the secret number   Displays "Too high! Try again."
  Guess correctly                 Shows success message and attempt count; game ends
  Make multiple guesses           Attempt counter increases each time

## Limitations

-   The program expects integer input. Letters or decimal values cause a
    `ValueError`.
-   There is no maximum attempt limit; the game continues until the
    correct number is guessed.

## Author

Akash Adepu\
Python Programming Internship --- Day 5 of 45
