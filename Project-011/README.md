# Number Guessing Game 🎮🔢

Welcome to the **Number Guessing Game**! This is a simple Python-based game where you try to guess a randomly generated number within a set number of attempts based on the difficulty level.

## 📝 Description

The **Number Guessing Game** challenges you to guess a randomly generated number between 1 and 100. You can choose between two difficulty levels:

- **Easy**: 10 attempts to guess the number.
- **Hard**: 5 attempts to guess the number.

### How the Game Works:
1. The computer generates a random number between 1 and 100.
2. You are given a set number of attempts to guess the number.
3. After each guess, the game will tell you whether your guess is too high, too low, or correct.
4. If you guess correctly, you win! If you run out of lives, you lose.

### Example:
1. You choose "easy" difficulty, giving you 10 lives.
2. The random number is `42`.
3. You guess `30`, and the game responds with "Too low."
4. You guess `50`, and the game responds with "Too high."
5. Finally, you guess `42`, and the game responds with "You guessed it right!"

## 🖥️ Code Overview

The program is structured with the following key components:

1. **Random Number Generation**:
   - The `randint()` function is used to generate a random number between 1 and 100.
2. **User Input**:
   - The program asks the user to choose a difficulty level (easy or hard) and then repeatedly asks the user to guess the number.
3. **Game Loop**:
   - The game continues until the user guesses the correct number or runs out of lives.
4. **Feedback**:
   - After each guess, the program provides feedback on whether the guess is too high, too low, or correct.

## 🛠️ How It Works:

1. **Difficulty Level**:
   - The player chooses between "easy" or "hard" difficulty, which determines the number of attempts (lives) they have.
2. **Guessing**:
   - The player guesses a number, and the game checks if it's correct, too high, or too low.
3. **Lives**:
   - The player loses one life after each incorrect guess.
4. **Game End**:
   - The game ends when the player guesses the number correctly or runs out of lives.

## 📂 Folder Structure

- `main.py`: Contains the main code for the project.

## 💡 Features

- Allows the player to choose between easy or hard difficulty.
- Provides feedback on whether the guess is too high, too low, or correct.
- Tracks the number of lives and ends the game when the player runs out of lives or guesses correctly.

## 🌟 Future Enhancements

- Add an option to replay the game without restarting the program.
- Implement a scoring system based on the number of attempts used.
- Add a graphical user interface (GUI) for a more interactive experience.

## 📜 License

This project is open-source and licensed under the MIT License.
