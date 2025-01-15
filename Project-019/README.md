# Pong Game 

Welcome to the **Pong Game**! This Python game is based on the classic Pong, where two paddles control the movement of the ball, and the objective is to score by hitting the ball past the opponent's paddle.

## 📝 Description

This game allows users to:
- Control two paddles (one on the left and one on the right) to bounce the ball.
- Score points by getting the ball past the opponent's paddle.
- Track the score for both players and display the current score during the game.

### How the Game Works:
1. The game begins with a ball in the center and two paddles on either side.
2. Players control the paddles:
   - The left paddle is controlled using `W` (up) and `S` (down).
   - The right paddle is controlled using the `Up` and `Down` arrow keys.
3. The ball moves and bounces off the walls and paddles.
4. When the ball goes past a paddle, the opponent scores a point.
5. The game continues until the player exits.

### Example:
- If the ball hits the top or bottom walls, it bounces off.
- If the ball hits the left or right walls, the opponent scores a point, and the ball is reset to the center.

## 🖥️ Code Overview

The program is organized into multiple files and classes, each serving a specific purpose:

### 1. **Ball Class (`ball.py`)**:
   - **Attributes**:
     - `x_move`, `y_move`: The movement of the ball along the x and y axes.
     - `move_speed`: The speed at which the ball moves.
   - **Methods**:
     - `move()`: Moves the ball based on the current direction and speed.
     - `bounce_y()`: Reverses the ball's vertical direction.
     - `bounce_x()`: Reverses the ball's horizontal direction and increases its speed.
     - `reset_position()`: Resets the ball to the center after scoring.

### 2. **Bricks Class (`bricks.py`)**:
   - **Attributes**:
     - `POSITION`: The starting position of the paddle (brick).
   - **Methods**:
     - `create_brick()`: Creates the paddle (brick) with a given position.
     - `brick_up()`, `brick_down()`: Moves the paddle up or down.

### 3. **ScoreCard Class (`scoreboard.py`)**:
   - **Attributes**:
     - `l_score`, `r_score`: The scores for the left and right players.
   - **Methods**:
     - `update_scoreboard()`: Updates and displays the current scores on the screen.
     - `point_l()`, `point_r()`: Increases the left or right player's score.

### 4. **Main Program (`main.py`)**:
   - The main script that runs the game, interacting with the `Ball`, `Bricks`, and `ScoreCard` classes.
   - It sets up the screen, listens for key presses to control the paddles, and manages the game loop.

## 📂 Folder Structure

- `ball.py`: Contains the `Ball` class that models the ball and its movement.
- `bricks.py`: Contains the `Bricks` class that models the paddles and their movement.
- `scoreboard.py`: Contains the `ScoreCard` class that tracks and displays the score.
- `main.py`: The main script that runs the game and interacts with the other classes.

## 💡 Features

- **Real-Time Gameplay**: The game runs in real-time, with the ball moving and bouncing off the walls and paddles.
- **Score Tracking**: The game tracks the score for both players and updates the scoreboard during the game.
- **Player Control**: Players control the paddles using keyboard keys to move them up and down.
- **Game Reset**: When the ball passes a paddle, the game resets the ball to the center and updates the score.

## 🌟 Future Enhancements

- **Multiple Difficulty Levels**: Add difficulty levels by adjusting the speed of the ball and paddles.
- **Sound Effects**: Add sound effects for when the ball bounces or when a player scores.
- **Game Restart**: Allow players to restart the game after a match ends.
- **Multiplayer Mode**: Add a multiplayer mode for local network play.

## 📜 License

This project is open-source and licensed under the MIT License.
