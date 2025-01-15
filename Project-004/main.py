#Rock, Paper, Scissors Game

import random

def RPSGame() :
    list_of_RPS = ["rock", "paper", "scissors"]
    user_RPS = input("What You Choose??\n").lower()
    random_RPS = random.choice(list_of_RPS)
    print(random_RPS)
    if user_RPS == "rock" :
        if random_RPS == "rock" :
            print("Draw\n")

        elif random_RPS == "paper" :
            print("Computer Wins\n")

        else :
            print("You Win\n")

    elif user_RPS == "paper" :
        if random_RPS == "paper" :
            print("Draw\n")

        elif random_RPS == "rock" :
            print("You Win\n")

        else :
            print("Computer Wins\n")

    else :
        if random_RPS == "scissors" :
            print("Draw\n")

        elif random_RPS == "rock" :
            print("Computer Wins\n")

        else :
            print("You Win\n")

    return 0

result = RPSGame()
print(result)