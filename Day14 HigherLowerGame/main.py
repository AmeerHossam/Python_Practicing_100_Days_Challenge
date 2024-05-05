import ascii
import game_data
import random
import os
# Format the account data into printable format.
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    ### Take the user answer
    if a_followers > b_followers:
        return guess == "a"  #True if the user enter a
    else:
        return guess == "b"
#Display Art
print(ascii.higher_lower)
score = 0
game_running = True
account_B = random.choice(game_data.data)
# Make the game repeatable
while game_running:
    # Generate a random account from the game data
    # Make the account at position B become the next account at position A
    account_A = account_B
    
    while account_A == account_B:
        account_B = random.choice(game_data.data)



    print(f"Compare A: {format_data(account_A)}")
    print(ascii.vs)
    print(f"Against B: {format_data(account_B)}")

    # Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()



    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    # Give user feedback on their guess
    # Score keeping
    os.system("cls" if os.name == "nt" else "clear")
    if is_correct:
        score += 1
        print(f"You're right, your current score is {score}")
    else:
        print(f"Sorry, You're wrong, your final score is {score}")
        game_running = False




    # Clear the screen between rounds