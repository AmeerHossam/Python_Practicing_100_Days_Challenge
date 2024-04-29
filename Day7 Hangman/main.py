import random,stages,word_list
print(stages.logo)
chosen_word = random.choice(word_list.word_list)
length_of_word = len(chosen_word)
print(f"Hello, You have to guess the word, It contains {length_of_word} letters")
blank=["_"]*length_of_word
print(chosen_word)
lifes = 6
end_of_game = False
while not end_of_game:
    letter_guess = input("Please enter a letter:\n>>").lower()

## To put the correct letter instead of the blank symbol
    for position in range(length_of_word):
            
        if letter_guess == chosen_word[position]:
            blank[position]=letter_guess
    
    print(blank)

## Check if the player checked the word correct
    if "_" not in blank:
        print("Well done, you checked the word correctly!!")
        end_of_game = True

##Tracking the player lives
    if letter_guess not in chosen_word:
        print(f"You lost a life, you still have {lifes} chances")
        print(stages.stages[lifes])
        lifes -= 1

        if lifes < 0:
            print("You have lost")
            end_of_game = True