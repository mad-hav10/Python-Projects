#Hangman
import random

print("Welcome to Hangman\n")

list_of_words = ["mathematics", "cat", "tool", "plastic", "apple"]
random_word = random.choice(list_of_words)
list_of_letters = list(random_word)
blanks = []
lives = 6

for i in range(0, len(list_of_letters)) :
    blanks.append("_")

print(" ".join(blanks))
while lives > 0:
    guess = input("Guess a letter you think is there in the word\n")
    if guess in list_of_letters :
        for i in range(0, len(list_of_letters)) :
            if list_of_letters[i] == guess :
                blanks[i] = guess
        print("Correct Guess\n")
                
    else :
        lives -= 1
        print("Wrong Guess\n")

    print(" ".join(blanks))

    if "_" not in blanks :
        print("You Win\n")
        break

if lives == 0 :
    print("You Lose\n")
