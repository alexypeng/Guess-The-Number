# Number guessing game created by Alexander Peng

import random
from art import logo

EASY_MODE_LIVES = 10
HARD_MODE_LIVES = 5

def check_guess(guess, answer, turns_left):
    """Checks if the player's guess matches the correct answer"""
    
    if guess == answer:
        print("You got the answer!")
        return -1
    elif guess > answer:
        print("Too high!")
        return turns_left - 1
    else:
        print("Too low!")
    return turns_left - 1

def set_difficulty(difficulty):
    """Sets the number of lives based on the difficulty chosen by the player"""
    if difficulty.lower() == "easy":
        return 10
    else:
        return 5

def game():
    """Main function for running the number guessing game"""
    answer = random.randint(1, 100)
    
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print(answer)

    lives = set_difficulty(input("Please choose a difficulty. 'easy' for easy, and 'hard' for hard: "))

    got_answer = False
    
    while lives > 0 and not got_answer:
        print(f"You have {lives} guesses remaining.")
        guess = int(input("Please guess a number from 1 to 100: "))

        guess_right = check_guess(guess, answer, lives)
        
        if guess_right == -1:
            got_answer = True
        else:
            lives = check_guess(guess, answer, lives)

    if lives == 0:
        print("Too bad! You ran out of guesses. Try again next time!")

game()