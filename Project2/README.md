# Tip Calculator 💰💡

Welcome to the **Tip Calculator**! This simple Python project calculates the tip and splits the bill among multiple people based on user input.

## 📝 Description
The **Tip Calculator** takes the total bill amount, the tip percentage, and the number of people to split the bill between. It then calculates the amount each person should pay, including the tip.

## 🚀 How It Works
The program defines a function `TipCalculator()` that:
- Takes three inputs: `bill` (total amount of the bill), `tip` (tip percentage), and `people` (number of people to split the bill).
- Calculates the total bill after adding the tip.
- Splits the total bill after tip among the specified number of people.
- Returns the amount each person should pay.

### Sample input and output:
- **Input**: 
  - Bill: `$100`
  - Tip: `15%`
  - People: `4`
- **Output**: 
  - Each person pays: `$28.75`

## 🖥️ Code Example
```python
# Tip Calculator
def TipCalculator():
    bill = float(input("Enter the total amount of bill to be paid\n"))
    tip = float(input("Enter the percent of tip you want to give\n"))
    people = float(input("Enter the number of people you want to split the bill in\n"))

    bill_after_tip = bill + ((tip/100)*bill)
    splited_bill = bill_after_tip/people
    return [splited_bill]

result = TipCalculator()
print(result)
```

## 📂 Folder Structure
- `main.py`: Contains the main code for the project.

## 💡 Features
- Calculates the tip and splits the bill.
- Takes dynamic input from the user for customization.
- Easy to use and modify for personalized results.

## 🌟 Future Enhancements
- Add error handling for invalid inputs (e.g., non-numeric values).
- Allow the user to round the split amount to a certain decimal point.

## 📜 License

This project is open-source and licensed under the MIT License.
