# Programmer: Madelyn Hershberger
# Date: 2.29.2024
# Program: AI Playground

print('This will be a place for me to play with programming using AI Technology\n')

import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess the number between 1 and 10: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        else:
            print("Incorrect guess. Try again.")

guess_number()
