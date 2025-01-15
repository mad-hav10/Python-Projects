# Blackjack Game 🃏♠️

Welcome to the **Blackjack Game**! This is a simple Python-based game where you compete against the dealer to get as close to 21 as possible without going over. 

## 📝 Description

The **Blackjack Game** simulates a basic version of the card game Blackjack. The player (you) competes against the dealer. You can choose to draw additional cards or hold your current hand, while the dealer automatically draws cards until their score is 17 or higher.

### How the Game Works:
1. Both the player and the dealer are dealt two cards.
2. The player can choose to "hit" (draw another card) or "stand" (keep the current hand).
3. The dealer must continue drawing cards until their hand is worth 17 or more.
4. The goal is to get a hand value as close to 21 as possible, without going over.
5. The winner is determined based on who has the highest hand value under 21, or the dealer loses if they exceed 21.

## 🚀 How It Works

1. **Card Dealing**: The `deal_card()` function randomly selects a card from a list of possible values.
2. **Score Calculation**: The `calculate_score()` function calculates the score of the player's or dealer's hand. A special case is handled if an Ace (represented as 11) causes the score to exceed 21, converting it to 1.
3. **Game Flow**: The game continues until the player or dealer wins or loses based on the rules. The dealer draws cards automatically until their score is 17 or more.

### Example:
1. Player receives cards: `[10, 7]`, sum = `17`.
2. Dealer receives cards: `[8, 5]`, sum = `13`.
3. Player chooses to "hit" and receives a `3`, making the hand `[10, 7, 3]`, sum = `20`.
4. Dealer draws cards until their score is `17`.
5. The winner is determined based on the scores.

## 🖥️ Code Overview

The program is structured with the following key components:

1. **Card Dealing**: 
   - `deal_card()` randomly selects a card from a predefined list of values.
2. **Score Calculation**:
   - `calculate_score()` computes the total value of a hand and handles special cases for Blackjack and Ace cards.
3. **Comparison**:
   - `compare()` compares the player's and dealer's scores and returns the result of the game (win, loss, or draw).
4. **Game Loop**:
   - The game runs in a loop until the player decides to stand or the game is over.
5. **Dealer Logic**:
   - The dealer draws cards until their score is at least 17.

You can find the complete implementation in the `main.py` file.

## 📂 Folder Structure

- `main.py`: Contains the main code for the project.

## 💡 Features

- Allows the player to draw additional cards or stand.
- Simulates the dealer's automatic behavior based on Blackjack rules.
- Handles edge cases like Blackjack and the Ace card being worth 1 or 11.

## 🌟 Future Enhancements

- Add betting and a player balance system.
- Implement a graphical user interface (GUI) for a more interactive experience.
- Allow the player to play multiple rounds in one session.

## 📜 License

This project is open-source and licensed under the MIT License.
