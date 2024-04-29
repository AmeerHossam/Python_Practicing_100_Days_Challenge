print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
while True:
    first_decision=input("You're at a cross road. Where do you want to go? Type 'left' or 'right\n>>").lower()
    if first_decision == "right":
        print("Fall into a hole, Game Over")
        break
    elif first_decision == "left":
            second_decision=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boad. Type 'swim' to swim across.\n>>").lower()
            if second_decision == "wait":
                    third_decision=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n>>")
                    if third_decision == "red":
                        print("Burned by fire. Game Over.")
                        break
                    elif third_decision == "yellow":
                        print("Congratulations, YOU WON!!!")
                        break
                    elif third_decision == "blue":
                        print("Eaten by beasts, Game Over")
                        break
                    else:
                        print("Wrong choice")
            elif second_decision == "swim":
                print("Attacked by trout. Game Over.")
                break
            else:
                print("Enter a correct choice, Try again")
    else:
        print("Wrong Choice, Try again.")