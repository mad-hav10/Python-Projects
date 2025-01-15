#Number Guessing Game

import random
from random import randint

print("Welcome to Number Guessing game\n")
difficulty = input('Enter the difficulty you want, easy or hard\n').lower()
random_num = randint(1, 100)
print(random_num)
if difficulty == "easy" :
    total_lives = 10
else :
    total_lives = 5

while total_lives > 0 :
    guess = int(input("Guess The no. you think it is\n"))
    if guess == random_num :
        print('You guessed it right\n')
        break
    if guess < random_num :
        print("Too Low\n")
        total_lives -= 1
        print(total_lives)
    else :
        print('Too high\n')
        total_lives -= 1
        print(total_lives)

print('You ran out of lives\n')