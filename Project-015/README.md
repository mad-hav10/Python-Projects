# Quiz Game: True/False Questions

Welcome to the **Quiz Game**! This Python program presents True/False questions from various categories and tracks the user's score as they progress through the quiz.

## 📝 Description

This program allows users to:
- Answer a series of True/False questions.
- Track their score after each question.
- See their final score after completing the quiz.

### How the Program Works:
1. The program loads a list of questions (from a `data.py` file).
2. Each question is presented to the user, and they are prompted to answer "True" or "False".
3. The program checks if the user's answer is correct and updates the score.
4. Once all questions are answered, the program displays the final score.

### Example:
- If the user answers correctly, their score increases by 1.
- If the user answers incorrectly, their score remains the same.
- After all questions have been answered, the final score is displayed.

## 🖥️ Code Overview

The program is organized into multiple files and classes, each serving a specific purpose:

### 1. **Question Class (`question_model.py`)**:
   - **Attributes**:
     - `text`: The question text.
     - `answer`: The correct answer to the question (True/False).
   - **Methods**:
     - `__str__()`: Returns a string representation of the question and its answer.

### 2. **QuizBrain Class (`quiz_brain.py`)**:
   - **Attributes**:
     - `question_number`: Tracks the current question number.
     - `question_list`: The list of all questions in the quiz.
     - `choice`: Stores the user's answer to the current question.
     - `score`: Tracks the user's score.
   - **Methods**:
     - `next_question()`: Displays the next question and takes the user's answer.
     - `score_checking()`: Checks if the user's answer is correct and updates the score.
     - `game_complete()`: Displays the final score when the quiz is complete.

### 3. **Data File (`data.py`)**:
   - Contains a list of questions, each with a category, difficulty, and the correct answer.

### 4. **Main Program (`main.py`)**:
   - The main script that runs the quiz, interacting with the `Question` and `QuizBrain` classes.
   - It loads the questions from `data.py`, initializes the quiz, and presents the questions to the user one by one.

## 📂 Folder Structure

- `data.py`: Contains the question data in a list of dictionaries format.
- `question_model.py`: Contains the `Question` class that models individual questions.
- `quiz_brain.py`: Contains the `QuizBrain` class that manages the quiz logic.
- `main.py`: The main script that runs the quiz and interacts with the other classes.

## 💡 Features

- **Modular Design**: The program is divided into multiple classes for better maintainability and clarity.
- **Question Bank**: A list of questions with categories and difficulty levels (though currently all are easy).
- **Score Tracking**: The program tracks and displays the user's score after each question and at the end of the quiz.

## 🌟 Future Enhancements

- **Multiple Difficulty Levels**: Add more difficulty levels (e.g., Medium, Hard) to the questions.
- **Timed Quiz**: Implement a timer to limit the time for answering each question.
- **User Accounts**: Implement user accounts and track their quiz history and scores.
- **Graphical User Interface (GUI)**: Build a GUI to make the quiz more interactive and visually appealing.

## 📜 License

This project is open-source and licensed under the MIT License.
