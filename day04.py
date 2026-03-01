import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = [Rock, Paper, Scissors]

print("Rock... Paper... Scissors!\n"
      "_________ARE______________\n"
      "_________YOU______________\n"
      "________READY?____________\n")


player_pick = int(input("Type 1 for Rock, 2 for Paper, or 3 for Scissors: "))
player_pick -= 1

computer_pick = random.randint(0, 2)

while player_pick != 0 and player_pick !=2 and player_pick != 3:
    print("Invalid choice!")
    player_pick = int(input("Type 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    player_pick -= 1

else:
    print(moves[player_pick])

print("Computer picks:\n" + moves[computer_pick])
if player_pick == computer_pick:
    print("Draw!")
elif player_pick == 0 and computer_pick == 1:
    print("You lose!")
elif player_pick == 0 and computer_pick == 2:
    print("You win!")
elif player_pick == 1 and computer_pick == 0:
    print("You win!")
elif player_pick == 1 and computer_pick == 2:
    print("You lose!")
elif player_pick == 2 and computer_pick == 0:
    print("You lose!")
elif player_pick == 2 and computer_pick == 1:
    print("You win!")

print("Play again soon!")
