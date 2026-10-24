import random

number = random.randint(1,100)
total = 0

print("Guess the number between 1 to 100")

while True:
    user = int(input("Enter your number: "))
    total =+ 1
    if user == number:
        print(f"Correct! You found the number: {number}")
        print(f"Attempts taken: {total}")
        
        break
    elif user < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
