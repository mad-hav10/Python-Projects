# Hangman Game 🎯🎮

Welcome to the **Hangman Game**! Test your word-guessing skills in this classic game where you try to uncover the hidden word before running out of lives.

## 📝 Description

The **Hangman Game** challenges players to guess the letters in a randomly chosen word. Each incorrect guess costs a life, and the player wins by correctly identifying the word before their lives run out.

## 🚀 How It Works

The program:
1. Selects a random word from a predefined list of words.
2. Displays blanks representing the hidden letters of the word.
3. Prompts the player to guess letters one at a time.
4. Updates the blanks with correctly guessed letters or reduces lives for incorrect guesses.
5. Ends the game with a win if the word is guessed or a loss if lives run out.

### Sample Gameplay:
- **Word**: `apple`
- **Initial Display**: `_ _ _ _ _`
- **Player Guess**: `a`
- **Updated Display**: `a _ _ _ _`

## 🖥️ Code Overview

The **Hangman Game** is implemented in Python. Below is a brief overview of the key parts of the code:

1. **Word Selection**:
   - A random word is selected from a predefined list of words.
2. **Blanks Initialization**:
   - Blanks (`_`) are displayed to represent each letter of the word.
3. **Guess Evaluation**:
   - If the guessed letter is in the word, it updates the blanks.
   - If the guessed letter is not in the word, the player loses a life.
4. **Game End Conditions**:
   - The player wins if all blanks are filled.
   - The player loses if they run out of lives.

You can view the full code in the `main.py` file in the repository.

## 📂 Folder Structure

- `main.py`: Contains the main code for the project.

## 💡 Features

- Randomly selects words for replayability.
- Tracks and displays progress with blanks and guessed letters.
- Provides feedback for correct and incorrect guesses.

## 🌟 Future Enhancements

- Add difficulty levels with varying word lengths and lives.
- Include a graphical interface for a more interactive experience.
- Allow players to input their own word list.

## 📜 License

This project is open-source and licensed under the MIT License.
