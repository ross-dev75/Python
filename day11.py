import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/ 
"""

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def total_score(hand):
    total = 0
    for card in hand:
        total += card
    return total


def blackjack():
    print(logo)
    players_hand =[]
    computers_hand =[]
    # get player cards and score
    players_hand.append(get_card())
    players_hand.append(get_card())
    player_score = total_score(players_hand)
    # get computer card and initial score
    computers_hand.append(get_card())
    computer_score = total_score(computers_hand)
    #show cards, score
    print(f"Your cards: {players_hand}")
    print(f"Your current score is {player_score}")
    print(f"Computer's first card: [{computers_hand[0]}]")
    # account for the 'ace', which starts with a value of 11 and decreases to a value of 1 as-needed
    ace_high = False
    for card in players_hand:
        if card == 11:
            ace_high = True
    # did the player get an ace and a face card? game over, they win! if not, 'play on'...
    play_on = True
    if player_score == 21:
        play_on = False


    # let's play the game!
    while play_on and player_score < 21:
        draw = input("type 'y' to get another card. type 'n' to pass: ")

        if draw == "y":
            if ace_high:
                # if the ace is high and the player 'busts', we need to reduce the value of the ace to 1.
                players_hand.append(get_card())
                player_score = total_score(players_hand)
                if player_score > 21:
                    for card in players_hand:
                        if card == 11:
                            players_hand.remove(card)
                            players_hand.append(1)
                            player_score = total_score(players_hand)
                print(f"Your cards: {players_hand}")
                print(f"Your current score is {player_score}")
            else:
                players_hand.append(get_card())
                player_score = total_score(players_hand)
                print(f"Your cards: {players_hand}")
                print(f"Your current score is {player_score}")


        if draw == "n":
            # if the player stops drawing cards and isn't at or over 21, it's the computers turn to draw.
            while computer_score < 19:
                computers_hand.append(get_card())
                computer_score = total_score(computers_hand)
                print(f"Computer cards: {computers_hand}")
                print(f"Computer current score is {computer_score}")
                play_on = False

    if player_score > 21:
        print("\n")
        print(f"Your final hand: {players_hand}, final score: {player_score}")
        print("\n")
        print("Your score is higher than 21.")
        print("You went over! YOU LOSE!! :(")
        print("\n")
        print(f"The computer wins with {computers_hand}, scoring {computer_score}")
    elif player_score == 21:
        print("\n")
        print(f"Your final hand: {players_hand}")
        print(f"Computer's final hand: {computers_hand}, final score: {computer_score}")
        print("\n")
        print(f"Your total score is {player_score}. YOU WIN !!! :)")
    elif player_score < computer_score:
        if computer_score > 21:
            print("\n")
            print(f"Your final hand: {players_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computers_hand}, final score: {computer_score}")
            print("\n")
            print("Computer went over! YOU WIN !!! :)")
        else:
            print("\n")
            print(f"Your final hand: {players_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computers_hand}, final score: {computer_score}")
            print("\n")
            print("You were beat by the computer! YOU LOSE!! :(")
    elif player_score == computer_score:
        if player_score < 21:
            print(f"Your final hand: {players_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computers_hand}, final score: {computer_score}")
            print("\n")
            print("Player and Computer draw! Play again soon!")
    else:
        print("Unexpected Error")

prompt = True
while prompt:
    answer = input("Do you want to play Blackjack? Type 'yes' or 'no': ")
    if answer == "yes":
        blackjack()
        prompt = False
    elif answer == "no":
        prompt = False
    else:
        print("Invalid input.")


