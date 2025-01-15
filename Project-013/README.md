# Coffee Machine Simulator ☕️

Welcome to the **Coffee Machine Simulator**! This program allows you to choose between different types of coffee (Espresso, Latte, and Cappuccino), checks if there are enough resources, and accepts payments to make the coffee. The program also keeps track of the resources and money.

## 📝 Description

This program simulates a coffee machine where:
- The user can select from three coffee types: Espresso, Latte, and Cappuccino.
- The program checks if there are enough resources (water, milk, and coffee).
- The user enters the amount of money they want to insert, and the program calculates whether the amount is sufficient to make the selected coffee.
- If the user inserts enough money, the machine makes the coffee, deducts the ingredients, and updates the resources.
- The program also tracks the total money made.

### How the Program Works:
1. The user selects a coffee option: Espresso, Latte, or Cappuccino.
2. The program checks if there are enough resources to make the selected coffee.
3. The user inserts coins (pennies, nickels, dimes, and quarters).
4. The program calculates if the inserted money is sufficient.
5. If the payment is sufficient, the program makes the coffee, updates the resources, and adds the payment to the total money.
6. The user can also type "report" to view the remaining resources and total money made.

### Example:
- If the user selects "Latte", the program will check if there is enough water, milk, and coffee.
- If the user has enough money (e.g., $2.5 for a latte), the machine will deduct the ingredients, make the coffee, and give the change if needed.

## 🖥️ Code Overview

The program is structured as follows:

1. **Menu**:
   - The `MENU` dictionary contains the coffee options (Espresso, Latte, and Cappuccino) along with their ingredients and costs.
   
2. **Resources**:
   - The `resources` dictionary keeps track of the available stock of water, milk, and coffee. These resources are reduced when a coffee is made.

3. **Money**:
   - The `money` dictionary keeps track of the total money earned by the coffee machine.

4. **Functions**:
   - `report(resources, money)`: Displays the current resources and total money.
   - `resource_check(resources, choice)`: Checks if there are enough ingredients to make the selected coffee.
   - `coin_calculate(choice, pennies, nickles, dimes, quarters, money)`: Calculates if the inserted money is sufficient to make the selected coffee and provides change if necessary.
   - `ingridents_check(resources, choice)`: Deducts the required ingredients from the resources when a coffee is made.

5. **Main Loop**:
   - The program runs in a loop where the user can select a coffee type, check resources, and insert money.
   - If the user enters "report", the current status of resources and money is displayed.
   - The loop continues until the user decides to power off.

## 📂 Folder Structure

- `data.py`: Contains the coffee menu, resources, and money.
- `main.py`: The main script that runs the coffee machine simulation, handles user input, checks resources, and processes payments.

## 💡 Features

- Select from three types of coffee: Espresso, Latte, and Cappuccino.
- Check available resources before making a coffee.
- Enter coins (pennies, nickels, dimes, and quarters) to pay for coffee.
- View remaining resources and total money made with the "report" command.
- Keep track of resources and money throughout the program.

## 🌟 Future Enhancements

- Add more coffee types to the menu.
- Implement a GUI for a more interactive experience.
- Add a system for restocking resources automatically.
- Introduce a system for user accounts and saving preferences.

## 📜 License

This project is open-source and licensed under the MIT License.
