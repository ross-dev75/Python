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
    """ Draw's a card from a list of numbers representing one complete suit."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)



def total_score(hand):
    """Calculates the total score given a hand. If there's an ace in the hand (11) and the total score goes over 21,
    the value of the ace changes to (1)"""
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)



def compare_scores(player_score, computer_score):
    """Compares the user score against the computer score. Prints both. Shows winner."""
    if player_score == computer_score:
        print(f"\nPlayer scores {player_score}. Computer scores {computer_score}. Draw!")
    elif player_score > 21:
        print(f"\n Player scores {player_score}. Computer scores {computer_score}. You went over! You lose!")
    elif player_score == 21:
        print(f"\nPlayer scores {player_score}. Computer scores {computer_score}. Blackjack! You win!")
    elif player_score > computer_score:
        print(f"\nPlayer scores {player_score}. Computer scores {computer_score}. You win!")
    elif player_score < computer_score:
        if computer_score > 21:
            print(f"\nPlayer scores {player_score}. Computer scores {computer_score}. Computer went over! You Win!")
        elif computer_score == 21:
            print(f"\nPlayer scores {player_score}. Computer scores {computer_score}. Computer gets Blackjack! You lose!")
        elif computer_score <= 20:
            print(f"Player scores {player_score}. Computer scores {computer_score}. You lose. Computer Wins!")
    else:
        print(f"Player scores {player_score}. Computer scores {computer_score}.\n\nScoring function error...")



def blackjack():
    """
    Game starts with two empty hands. Two cards delt to player and computer. Scores taken. Player cards revealed,
    computer's first card revealed. Player can end turn, or draw card(s). They can keep drawing cards until they end
    their turn by a) not drawing another card, or b) scoring over 21.
    Computer starts drawing when the player's turn is finished. If the computer has less than 18 points and less points
    than the player, it will draw as long as the player's total score wasn't higher than 21. The computer will otherwise
    end its turn.
    The game will print out the player and computer hands, calculate the scores, compare the scores, and declare
    a winner. The game will end.
    """
    print(logo)
    players_hand =[]
    computers_hand =[]

    for _ in range(2):
        players_hand.append(get_card())
        computers_hand.append(get_card())

    player_score = total_score(players_hand)
    computer_score = total_score(computers_hand)

    print(f"Your cards: {players_hand}")
    print(f"Your current score is {player_score}")
    print(f"Computer's first card: [{computers_hand[0]}]")

    play_on_player = True
    play_on_computer = False
    if player_score == 21:
        play_on_player = False

    while play_on_player:
        if player_score < 21:
            draw = input("type 'y' to get another card. type 'n' to pass: ")
            if draw == "y":
                players_hand.append(get_card())
                player_score = total_score(players_hand)
                print(f"Your cards: {players_hand}, your current score is {player_score}")

            if draw == "n":
                play_on_player = False
                play_on_computer = True
        elif player_score >= 21:
            play_on_player = False
            play_on_computer = True

    while play_on_computer:
        if computer_score < 18:
            if computer_score < player_score:
                if player_score <= 21:
                    computers_hand.append(get_card())
                    computer_score = total_score(computers_hand)
                else:
                    play_on_computer = False
            else:
                play_on_computer = False
        else:
            play_on_computer = False

    print(f"Players hand: {players_hand}")
    print(f"Computer's hand: {computers_hand}")
    compare_scores(player_score, computer_score)



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
