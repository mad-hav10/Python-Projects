# U.S. States Game 🗺️🇺🇸

Test your knowledge of U.S. geography with this interactive **U.S. States Game**! The goal is to name all 50 U.S. states by entering them one at a time. As you guess correctly, the names appear on the map in their respective locations.

## 📝 Description

The game displays a blank map of the United States and challenges players to:
- Guess the names of all 50 states.
- Receive visual feedback as correctly guessed states are displayed on the map.
- Track progress dynamically with a score counter.

### How It Works:
1. A blank U.S. map is displayed.
2. Players type their guesses in a text input box.
3. Correct guesses are marked on the map.
4. The game ends when all 50 states are correctly identified.

## 🖥️ Code Overview

The project is structured into two main components:

### 1. **Main Program (`main.py`)**
   - **Key Features**:
     - Displays the map using `turtle`.
     - Reads state data from a CSV file.
     - Tracks player guesses and dynamically updates the map.
   - **Core Functions**:
     - `screen.textinput()`: Collects user input.
     - State verification using a pandas DataFrame.
     - Displays guessed state names at their coordinates on the map.

### 2. **State Data (`50_states.csv`)**
   - A CSV file containing:
     - State names.
     - X and Y coordinates for each state's location on the map.

## 📂 Folder Structure

```
USStatesGame/
├── main.py
├── 50_states.csv
├── blank_states_img.gif
```

## 💡 Features

- **Interactive Gameplay**: Users can type state names, and the game dynamically responds to their input.
- **Progress Tracking**: The title bar shows the number of states guessed correctly.
- **Visual Feedback**: Correct guesses are marked on the map in real time.

## 🌟 Future Enhancements

- **Hint System**: Provide hints for unguessed states after a certain time.
- **Leaderboard**: Add a feature to track and display high scores.
- **State Facts**: Show interesting facts about a state when guessed correctly.
- **Timer**: Add a countdown timer for an additional challenge.

## 📜 License

This project is open-source and licensed under the MIT License.
