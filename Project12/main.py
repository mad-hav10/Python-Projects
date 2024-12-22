import random
from data import data
from logo import logo
from logo import vs

random1 = random.choice(data)
random2 = random.choice(data)

print(logo)
print()
print("Welcome to the High Low Game\n")
continue_game = False

random1_followers = random1['follower_count']
random2_followers = random2['follower_count']
while not continue_game :
    print(f"A: {random1['name']}, a {random1['description']}, from {random1['country']}")
    print(vs)
    print(f"B: {random2['name']}, a {random2['description']}, from {random2['country']}")
    choice = input("Compare Both on the basis of followers in insta and tell who has more followers\n").lower()
    if choice == "a" and random1_followers > random2_followers :
        random1 = random2
        random2 = random.choice(data)
    elif choice == "b" and random2_followers > random1_followers :
        random1 = random2
        random2 = random.choice(data)
    else :
        print("You Lost the game\n")
        continue_game = True
        