import random

secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed it!")
