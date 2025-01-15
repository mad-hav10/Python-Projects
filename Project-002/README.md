# Tip Calculator 💰🧮

Welcome to the **Tip Calculator**! This Python project helps you calculate the total bill, including a tip, and splits it evenly among a specified number of people.

## 📝 Description

The **Tip Calculator** is a handy tool for quickly determining how much each person needs to pay when splitting a bill. It calculates the total amount including a tip and divides it equally among the number of people.

## 🚀 How It Works

The program defines a function `TipCalculator()` that:
1. Takes three inputs from the user:
   - `bill`: The total bill amount.
   - `tip`: The percentage of the bill to give as a tip.
   - `people`: The number of people to split the bill among.
2. Calculates the total bill including the tip.
3. Divides the total bill by the number of people.
4. Returns the amount each person needs to pay.

### Sample input and output:
- **Input**: 
  - Bill = 100
  - Tip = 10%
  - People = 4
- **Output**: 
  - Each person pays: 27.5

## 🖥️ Code Overview

The **Tip Calculator** is implemented in Python. Below is a brief overview of the key parts of the code:

1. **`TipCalculator()`**: 
   - Prompts the user to input the total bill amount, tip percentage, and number of people.
   - Calculates the total bill with the tip and divides it among the specified number of people.
2. **Return Value**: Returns the amount each person needs to pay as a list (e.g., `[27.5]`).

You can view the full code in the `main.py` file in the repository.

## 📂 Folder Structure

- `main.py`: Contains the main code for the project.

## 💡 Features

- Calculates the total bill including the tip.
- Splits the bill evenly among the specified number of people.
- Simple and easy-to-use tool for group dining.

## 🌟 Future Enhancements

- Add error handling for invalid inputs (e.g., negative numbers or zero people).
- Provide a breakdown of the calculations for better transparency.
- Implement a graphical user interface for easier interaction.

## 📜 License

This project is open-source and licensed under the MIT License.
