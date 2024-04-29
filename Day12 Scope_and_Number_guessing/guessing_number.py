import msg , random
easy_level=10
hard_level=5

##Welcome Message
def welcome():
    print(msg.welcome_msg)

welcome()
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
##Generate a random number
number = random.randint(0,100)
print(f"{number}")

##Check the answer
def check_answer(user_num,number,chances):
    if user_num == number:
        print(f"Welldone, the number is {number}")
        return
    else:
        chances+=1
        if user_num < number:
            print("Your guess is less than the number")
        else:
            print("Your guess is higher than the number")
    return chances
##Easy
def easy_condition():
    chances = 0
    for n in range(0,easy_level):
        print(f"you've {easy_level-n} attempts remaining to guess the number")
        user_num = int(input("Guess the number:"))
        chances = check_answer(user_num,number,chances)
        if chances == easy_level:
            print("GameOver")
            break
##Hard
def hard_condition():
    chances = 0
    for n in range(0,hard_level):
        print(f"you've {hard_level-n} attempts remaining to guess the number")
        user_num = int(input("Guess the number:"))
        chances = check_answer(user_num,number,chances)
        if chances == hard_level:
            print("GameOver")
            break

if difficulty == "easy":
    easy_condition()

elif difficulty == "hard":
    hard_condition()
else:
    print("Please enter 'easy' or 'hard'")


