# Blackjack Game ♠️♦️

Welcome to the **Blackjack Game**! This is a Python implementation of the classic casino card game, where you try to get a hand value of 21 without exceeding it, while competing against the dealer.

## 📝 Description
In the **Blackjack Game**, you are dealt two cards initially, and you can choose to draw more cards to improve your hand. The dealer also draws cards but must stop once they reach a hand value of 17 or higher. The goal is to have a hand value as close to 21 as possible without going over. If you exceed 21, you lose the game.

## 🚀 How It Works
The program simulates a simple game of Blackjack with the following features:
1. Both the player and dealer are dealt two cards initially.
2. The player can choose to draw more cards or stop (pass).
3. The dealer must draw cards until they reach a score of 17 or higher.
4. The game ends when the player either exceeds 21, hits 21, or decides to stop. The dealer’s hand is revealed, and the winner is determined.

### Sample input and output:
- **Input**: 
  - Player’s action: Press `y` to draw another card, press `n` to pass.
- **Output**: 
  - Final result: User wins, loses, or draws based on their hand value and the dealer's hand.

## 🖥️ Code Overview
The **Blackjack Game** is implemented in Python. Below is a brief overview of the key parts of the code:

1. **`deal_card()`**: Randomly selects a card from the deck.
2. **`calculate_score()`**: Calculates the total score of the cards in hand, handling special cases like Aces.
3. **`compare()`**: Compares the user's score with the dealer's score to determine the winner.

## 📂 Folder Structure
- `main.py`: Contains the main code for the project.

## 💡 Features
- Simulates the Blackjack card game with user and dealer hands.
- Allows the user to make decisions during the game (draw cards or pass).
- Automatically handles dealer behavior (dealer stops drawing at 17 or higher).
- Compares the user’s hand to the dealer’s hand and announces the result.

## 🌟 Future Enhancements
- Implement a betting system for the player.
- Add the option to play multiple rounds or games.
- Improve the user interface with a graphical version of the game.

## 📜 License
This project is open-source and licensed under the MIT License.
