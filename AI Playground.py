# Programmer: Madelyn Hershberger
# Date: 2.29.2024
# Program: AI Playground

import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = input("Guess the number between 1 and 10 (or 'q' to quit): ")

        if guess.lower() == 'q':
            print("Thanks for playing!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        else:
            print("Incorrect guess. Try again.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        guess_number()
    else:
        print("Thanks for playing!")

print('Welcome to AI Playground!\nThis will be a place for me to play with programming using AI Technology\n')
guess_number()
