# Snake Game 🐍🎮

Welcome to the **Snake Game**! This is a modern implementation of the classic Snake game, where you guide a snake to eat food, grow longer, and aim for the highest score while avoiding collisions.

## 📝 Description

In this game, you control a snake that:
- Moves continuously in the chosen direction.
- Grows longer by eating food.
- Ends the game (or resets) if it collides with the wall or itself.

### Game Features:
1. **Score Tracking**:
   - The score increases when the snake eats food.
   - High scores are saved to a file and displayed on the screen.
2. **Food System**:
   - Randomly generated food items appear on the screen for the snake to consume.
3. **Snake Movement**:
   - The snake moves in one direction unless the player changes it using the arrow keys.
4. **Game Reset**:
   - The game resets automatically if the snake collides with the wall or itself.

## 🖥️ Code Overview

The project is divided into multiple files for better organization:

### 1. **Snake Class (`snake.py`)**
   - **Attributes**:
     - `segments`: A list of turtle objects representing the snake's body.
     - `head`: The first segment of the snake, which leads its movement.
   - **Methods**:
     - `create_snake()`: Initializes the snake with three segments.
     - `move()`: Moves the snake forward by updating each segment's position.
     - `add_segment(pos)`: Adds a new segment to the snake.
     - `extend()`: Extends the snake by adding a segment at the tail.
     - `reset()`: Resets the snake to its starting state after a collision.
     - Direction methods (`up`, `down`, `left`, `right`): Change the snake's movement direction.

### 2. **Food Class (`food.py`)**
   - **Attributes**:
     - Represents the food as a small blue circle.
   - **Methods**:
     - `refresh()`: Moves the food to a random location on the screen.

### 3. **Scoreboard Class (`scoreboard.py`)**
   - **Attributes**:
     - `score`: Tracks the current score.
     - `highscore`: Stores the highest score, read from and written to `data.txt`.
   - **Methods**:
     - `update_scoreboard()`: Updates the on-screen scoreboard.
     - `increase_score()`: Increases the score and updates the scoreboard.
     - `reset()`: Resets the current score and updates the high score if necessary.

### 4. **Main Program (`main.py`)**
   - The entry point of the game that ties all the components together.
   - **Key Features**:
     - Handles screen setup and listens for user inputs.
     - Manages the game loop, updating the screen and checking for collisions.

### 5. **Data File (`data.txt`)**
   - A text file used to store the high score.

## 📂 Folder Structure

```
SnakeGame/
├── snake.py
├── food.py
├── scoreboard.py
├── main.py
├── data.txt
```

## 💡 Features

- **Dynamic Gameplay**: The snake grows longer and moves faster as the game progresses.
- **Persistent High Score**: The game saves the highest score to `data.txt` for continuity.
- **Collision Detection**: Detects collisions with the wall or the snake's own body.

## 🌟 Future Enhancements

- **Obstacles**: Add random obstacles that the snake must avoid.
- **Game Modes**: Introduce difficulty levels or timed challenges.
- **Customizations**: Allow players to customize the snake's color or speed.
- **Multiplayer Mode**: Enable two players to control separate snakes.

## 📜 License

This project is open-source and licensed under the MIT License.
