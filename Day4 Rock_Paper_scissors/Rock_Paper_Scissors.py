import art
import random

game=[art.rock,art.paper,art.scissors]
random_check = random.randint(0,len(game)-1)

while True:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n>> "))
    print(f"your choice:\n{game[user_input]}")
    print(f"Computer's choice:\n{game[random_check]}")
    if user_input == 0 and random_check == 0:
        print("Try Again")
    elif user_input == 0 and random_check == 1:
        print("Computer wins")
        break
    elif user_input == 0 and random_check == 2:
        print("You win")
        break
    elif user_input == 1 and random_check == 0:
        print("You win")
        break
    elif user_input == 1 and random_check == 1:
        print("Try Again")
    elif user_input == 1 and random_check == 2:
        print("Computer wins")
        break
    elif user_input == 2 and random_check == 0:
        print("Computer wins")
        break
    elif user_input == 2 and random_check == 1:
        print("You win")
        break
    elif user_input == 2 and random_check == 2:
        print("Try again")
        
    else:
        print("You entered wrong input")