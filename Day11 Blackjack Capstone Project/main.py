import asciiArt as art
import random


# Create a deal_card() function that uses the list below to return a random card.
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def main():
    print(art.blackjack)

    # Deal the user and computer cards each using deal_card().
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        #Adding random cards to user and computer.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    #Create a function calculate the score for each user and computer.
    def calculate_score(cards):
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0
        
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    # Create a function compares between the user and computer scores.
    def compare_score(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "You lose, Computer has a blackjack"
        elif user_score == 0:
            return "Win, you got a blackjack"
        elif user_score > 21:
            return "You lose, you got more than 21"
        elif computer_score > 21:
            return "You win, Opponent went over"
        elif user_score > computer_score:
            return "You win"
        else:
            return "Computer wins"
    while not is_game_over:
        #Call calculate_score(). If the computer or user has a blackjack, or the score is above 21 >> end the game
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current_score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True

        else:
            user_should_deal = input("Typee 'y' for getting another card or 'n' to pass").lower()
            
        #if the game ius not ended, ask the user to pull another card. If yes
        #then use deal_card() to add another card
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play, the computer should keep drawing cards as long as less than 17

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer score is: {computer_score}, Your score is: {user_score}")
    print(compare_score(user_score, computer_score))

while input("Welcome to BlackJack game, Type y to start or no to quit (y/n): ").lower() == 'y':
    main()