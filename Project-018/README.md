# Snake Game 🐍

Welcome to the **Snake Game**! This Python game uses the Turtle graphics library, where the player controls a snake that grows longer each time it eats food. The objective is to avoid colliding with the walls and the snake's own body.

## 📝 Description

This game allows users to:
- Control a snake that moves around the screen.
- Eat food that appears at random positions to grow the snake and increase the score.
- Avoid collisions with the walls and the snake's own body to keep playing.
- Track the score during gameplay and display the final score when the game is over.

### How the Game Works:
1. The game begins with a snake of three segments.
2. The player controls the snake using the arrow keys to move up, down, left, or right.
3. Each time the snake eats food, it grows longer, and the score increases.
4. The game ends if the snake collides with the wall or itself.
5. The final score is displayed when the game is over.

### Example:
- If the snake eats food, it grows by one segment and the score increases by 1.
- If the snake collides with the wall or its own body, the game ends and the final score is shown.

## 🖥️ Code Overview

The program is organized into multiple files and classes, each serving a specific purpose:

### 1. **Snake Class (`snake.py`)**:
   - **Attributes**:
     - `segments`: A list of turtle objects representing the snake's body.
     - `head`: The head of the snake, which controls its movement.
   - **Methods**:
     - `create_snake()`: Initializes the snake with three segments.
     - `move()`: Moves the snake by updating the position of each segment.
     - `add_segment()`: Adds a new segment to the snake's body.
     - `extend()`: Extends the snake by one segment.
     - `up()`, `down()`, `left()`, `right()`: Methods to change the snake's direction.

### 2. **Food Class (`food.py`)**:
   - **Attributes**:
     - `shape`: The shape of the food, represented as a circle.
   - **Methods**:
     - `refresh()`: Moves the food to a random position on the screen.

### 3. **ScoreBoard Class (`scoreboard.py`)**:
   - **Attributes**:
     - `score`: The player's score.
   - **Methods**:
     - `update_scoreboard()`: Displays the current score on the screen.
     - `increase_score()`: Increases the score and updates the scoreboard.
     - `game_over()`: Displays a "Game Over" message when the game ends.

### 4. **Main Program (`main.py`)**:
   - The main script that runs the game, interacting with the `Snake`, `Food`, and `ScoreBoard` classes.
   - It sets up the screen, listens for key presses to control the snake, and manages the game loop.

## 📂 Folder Structure

- `food.py`: Contains the `Food` class that represents the food objects.
- `scoreboard.py`: Contains the `ScoreBoard` class that tracks and displays the score.
- `snake.py`: Contains the `Snake` class that models the snake and its movement.
- `main.py`: The main script that runs the game and interacts with the other classes.

## 💡 Features

- **Real-Time Gameplay**: The game runs in real-time, with the snake continuously moving until the game ends.
- **Snake Growth**: The snake grows longer as it eats food, making the game progressively more challenging.
- **Score Tracking**: The game tracks the player's score and displays it during the game and at the end.
- **Game Over**: The game ends when the snake collides with the wall or its own body, and the final score is displayed.

## 🌟 Future Enhancements

- **Levels**: Add multiple levels with increasing speed as the snake grows.
- **Sound Effects**: Add sound effects for eating food and collisions.
- **High Score**: Implement a high score tracker to save the highest score achieved.
- **Game Restart**: Allow players to restart the game without closing the program.

## 📜 License

This project is open-source and licensed under the MIT License.
