from random import randint

logo = r"""
  ________                              ___________.__              _______               ___.                ._._._.
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________| | | |
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ | | |
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\|\|\|
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   ______
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       \/\/\/
"""



EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5
ANSWER = randint(1, 100)



def check_answer(user_guess, actual_answer, turns):
    """ Checks users answer against actual answer, decreases turn count if wrong, returns num of turns remaining """
    if user_guess > actual_answer:
        print("You guessed too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("You guessed too low.")
        return turns - 1
    else:
        print(f"You guessed correctly! The answer was {actual_answer}.")
        return None



def set_difficulty():
    """ Sets difficulty to easy or hard mode """
    level = input("Choose a difficulty, 'easy' or 'hard': ")
    if level == "easy":
        return EASY_MODE_ATTEMPTS
    else:
        return HARD_MODE_ATTEMPTS



def game():
    print(logo)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"The answer is {ANSWER}")

    guess = 0
    turns = set_difficulty()
    while guess != ANSWER:
        if turns > 0:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            turns = check_answer(guess, ANSWER, turns)
        else:
            print(f"You ran out of guesses! The answer was {ANSWER}. Try again!")



game()



#  My initial code for this challenge is below. After completing this challenge and verifying my code works,
#  I watched the walkthrough solution video and realized I could have used more functions and global
#  variables to make this cleaner and neater. 
#
#
# import random
# 
# logo = r"""
#   ________                              ___________.__              _______               ___.                ._._._.
#  /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________| | | |
# /   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ | | |
# \    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\|\|\|
#  \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   ______
#         \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       \/\/\/
# """
# 
# secret_number = random.randint(1, 101)
# 
# 
# 
# def easy_mode():
#     lives = 10
#     while lives > 0:
#         print(f"You have {lives} attempts remaining to guess the number.")
#         player_guess = int(input("Make a guess: "))
#         if player_guess == secret_number:
#             print(f"Congratulations! You guessed the number {secret_number}!")
#             break
#         elif player_guess > secret_number:
#             print("Too High. Try again.")
#             lives -= 1
#         elif player_guess < secret_number:
#             print("Too Low. Try again.")
#             lives -= 1
#     if lives == 0:
#         print(f"You Lose! The number was {secret_number}\nYou ran out of lives. Restart the program to try again.")
# 
# 
# 
# def hard_mode():
#     lives = 5
#     while lives > 0:
#         print(f"You have {lives} attempts remaining to guess the number.")
#         player_guess = int(input("Make a guess: "))
#         if player_guess == secret_number:
#             print(f"Congratulations! You guessed the number {secret_number}!")
#             break
#         elif player_guess > secret_number:
#             print("Too High. Try again.")
#             lives -= 1
#         elif player_guess < secret_number:
#             print("Too Low. Try again.")
#             lives -= 1
#     if lives == 0:
#         print(f"You Lose! The number was {secret_number}\nYou ran out of lives. Restart the program to try again.")
# 
# 
# 
# prompt = True
# while prompt:
#     print(logo)
#     print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#     if difficulty != 'easy':
#         prompt = False
#         hard_mode()
#     else:
#         prompt = False
#         easy_mode()

