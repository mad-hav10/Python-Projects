#Blackjack Game

import random

def deal_card() :
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards) :
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)  

def compare(user_score, dealer_score) :
    if user_score == dealer_score :
        return "Draw"
    elif dealer_score == 21 :
        return "User Loses"
    elif user_score == 21 :
        return "User Wins"
    elif user_score > 21 :
        return "User Loses"
    elif dealer_score > 21 :
        return "User Wins"
    else :
        if user_score > dealer_score :
            return "User Wins"
        else :
            return "User Lose"

is_game_over = False
user_card = []
dealer_card = []

for _ in range(2) :
    user_card.append(deal_card())
    dealer_card.append(deal_card())

while not is_game_over :
    user_score = calculate_score(user_card)
    dealer_score = calculate_score(dealer_card)
    print(f'user cards : {user_card}, sum : {user_score}')
    print(f"Dealer 1st card : {dealer_card[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21 :
        is_game_over = True
    else :
        choice = input("Press y to draw another card else pree n to pass\n")
        if choice == "y" :
            user_card.append(deal_card())
        else :
            is_game_over = True

while dealer_score < 17 :
    dealer_card.append(deal_card())
    dealer_score = calculate_score(dealer_card)

print(f"User final Hand : {user_card}, sum : {user_score}")
print(f"Dealer Final hand : {dealer_card}, sum : {dealer_score}")
print(compare(user_score, dealer_score))