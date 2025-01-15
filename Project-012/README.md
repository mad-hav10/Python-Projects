# High Low Game 🎮📱

Welcome to the **High Low Game**! This is a fun and engaging game where you compare the Instagram followers of two random celebrities, athletes, or organizations. The goal is to correctly guess which one has more followers. The game continues until you make a wrong guess!

## 📝 Description

The **High Low Game** presents two random entities from a list of celebrities, athletes, musicians, and organizations, and asks you to guess which one has more Instagram followers. The game continues until you make an incorrect guess, and it then ends.

### How the Game Works:
1. The game displays two options, each representing a random entity (a person or organization).
2. You must guess which option has more Instagram followers.
3. If your guess is correct, the game continues with the same entity for one option, and a new entity is chosen for the second option.
4. If you guess incorrectly, the game ends and you lose.

### Example:
1. The game shows **A: Ariana Grande** and **B: Dwayne Johnson**.
2. You guess **A** (Ariana Grande), but if her followers are fewer than Dwayne Johnson's, you lose.

## 🖥️ Code Overview

The game consists of the following key components:

1. **Data**:
   - The `data.py` file contains a list of dictionaries, each representing a person or organization, with attributes like `name`, `follower_count`, `description`, and `country`.

2. **Game Logic**:
   - The `main.py` file imports the data and logo, selects two random entries from the `data.py` list, and presents them to the player.
   - The game asks the player to guess which entity has more Instagram followers.
   - The game continues if the player guesses correctly, updating one entity while choosing a new random one for the other.

3. **Visuals**:
   - The `logo.py` file contains the game's logo and the "vs" text that appears between the two options.

4. **Random Selection**:
   - The game randomly selects two entities from the data list, compares their follower counts, and prompts the player to choose which one has more followers.

5. **Feedback**:
   - The game gives feedback after each guess: if correct, it continues; if incorrect, the game ends with a loss message.

## 📂 Folder Structure

- `data.py`: Contains the data of celebrities and organizations, including their names, follower counts, and descriptions.
- `logo.py`: Contains the logo and "vs" text for the game.
- `main.py`: The main script that runs the game, handling logic and user input.

## 💡 Features

- Random selection of entities from a predefined list.
- Visual display of the entities with their descriptions and countries.
- User input to compare follower counts and make guesses.
- Continues the game with updated entities if the guess is correct.

## 🌟 Future Enhancements

- Add a scoring system based on the number of correct guesses.
- Display a leaderboard with high scores.
- Include more entities in the dataset to increase the variety of options.
- Implement a graphical user interface (GUI) for a more interactive experience.

## 📜 License

This project is open-source and licensed under the MIT License.
