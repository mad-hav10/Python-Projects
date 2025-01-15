# The Calculator Project 🔢💻

Welcome to the **Calculator Project**! This is a simple calculator built using Python that allows you to perform basic arithmetic operations like addition, subtraction, multiplication, and division.

## 📝 Description

The **Calculator Project** lets users perform multiple calculations without restarting the program. After performing an operation, you can either continue calculating with the result or start a new calculation.

### Operations Available:
- **Addition** (`+`)
- **Subtraction** (`-`)
- **Multiplication** (`*`)
- **Division** (`/`)

## 🚀 How It Works

The program:
1. Prompts the user to enter two numbers and choose an operation.
2. Performs the calculation and displays the result.
3. Asks if the user wants to continue with the result of the current operation or start a new calculation.

### Example:
1. User enters `5` and `3`, chooses the operation `+` (Addition).
2. The program displays `5 + 3 = 8`.
3. User decides to continue, and the next calculation is performed with `8`.

## 🖥️ Code Overview

The program is structured with the following key components:

1. **Functions for Basic Operations**:
   - `Addition()`, `Subtraction()`, `Multiplication()`, and `Division()` functions perform basic arithmetic.
2. **Main Calculation Logic**:
   - `Calculation()` determines which operation to perform based on the user input.
3. **Loop for Continuous Calculations**:
   - The program uses a `while` loop to allow the user to continue calculations until they decide to start a new one.
4. **User Interaction**:
   - The program prompts the user to input numbers, select an operation, and choose whether to continue with the result or start fresh.

You can find the complete implementation in the `main.py` file.

## 📂 Folder Structure

- `main.py`: Contains the main code for the project.

## 💡 Features

- Performs basic arithmetic operations.
- Allows the user to continue with the result of the previous calculation.
- User-friendly and interactive interface.

## 🌟 Future Enhancements

- Add support for more advanced mathematical functions (e.g., square roots, powers).
- Implement error handling for invalid inputs (e.g., dividing by zero).
- Enhance the user interface with a graphical front end.

## 📜 License

This project is open-source and licensed under the MIT License.
