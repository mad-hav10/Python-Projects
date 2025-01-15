# Coffee Machine Simulator ☕️

Welcome to the **Coffee Machine Simulator**! This Python program simulates a coffee machine where you can select from a menu of drinks, pay for your order, and receive your coffee if sufficient resources and payment are available.

## 📝 Description

This program allows users to:
- Choose from a menu of drinks (Latte, Espresso, and Cappuccino).
- Check if there are enough resources (water, milk, coffee) to make the selected drink.
- Insert coins to pay for the selected drink.
- Get a report of available resources and the current profit.
- Receive their drink if the payment is sufficient and resources are available.

### How the Program Works:
1. The user selects a coffee drink (Latte, Espresso, or Cappuccino).
2. The program checks if there are enough resources (water, milk, and coffee).
3. The user inserts coins (quarters, dimes, nickels, and pennies) to pay for the drink.
4. The program checks if the payment is sufficient and gives change if necessary.
5. If everything is in order, the coffee is made, resources are deducted, and the total profit is updated.

### Example:
- If the user selects "Latte", the program will check if there is enough water, milk, and coffee.
- If the user has enough money (e.g., $2.5 for a latte), the machine will deduct the ingredients, make the coffee, and provide any change if needed.

## 🖥️ Code Overview

The program is organized into three main classes: `CoffeeMaker`, `Menu`, and `MoneyMachine`. Here's an overview of each:

### 1. **CoffeeMaker Class**:
   - **Attributes**: 
     - `resources`: A dictionary that tracks the available resources (water, milk, coffee).
   - **Methods**:
     - `report()`: Displays the current resources available.
     - `is_resource_sufficient(drink)`: Checks if there are enough resources to make a particular drink.
     - `make_coffee(order)`: Deducts the required ingredients from the resources and makes the coffee.

### 2. **Menu Class**:
   - **Attributes**:
     - `menu`: A list of `MenuItem` objects (representing drinks).
   - **Methods**:
     - `get_items()`: Returns the names of all available menu items.
     - `find_drink(order_name)`: Finds and returns a specific drink based on the user's order.

### 3. **MoneyMachine Class**:
   - **Attributes**:
     - `profit`: Tracks the total profit made by the coffee machine.
     - `money_received`: Tracks the total amount of money inserted by the user.
   - **Methods**:
     - `report()`: Displays the current profit.
     - `process_coins()`: Accepts coins (quarters, dimes, nickels, pennies) and calculates the total amount inserted.
     - `make_payment(cost)`: Checks if the inserted money is sufficient for the selected drink. If sufficient, it deducts the cost and returns True, otherwise, it refunds the money and returns False.

### 4. **Main Program**:
   - The main program runs a loop where the user can select a drink, view reports, and make payments. The coffee machine will make the drink if the payment is sufficient and resources are available.

## 📂 Folder Structure

- `coffee_maker.py`: Contains the `CoffeeMaker` class that manages resources and makes coffee.
- `menu.py`: Contains the `MenuItem` and `Menu` classes, representing the menu and drink options.
- `money_machine.py`: Contains the `MoneyMachine` class that handles payments and profit tracking.
- `main.py`: The main script that runs the coffee machine, interacting with the user, menu, and other components.

## 💡 Features

- **Modular Design**: The program is divided into multiple classes for better maintainability and clarity.
- **Menu Selection**: Users can select from a variety of drinks.
- **Resource Management**: The program checks if there are enough resources to make a drink before proceeding.
- **Payment Handling**: Users can insert coins, and the program checks if the payment is sufficient.
- **Profit Tracking**: The program keeps track of the total profit earned from sales.

## 🌟 Future Enhancements

- **Additional Drink Options**: Add more drinks to the menu.
- **Refill System**: Automatically replenish resources when they run low.
- **User Accounts**: Implement user accounts and track their drink preferences and order history.
- **Graphical User Interface (GUI)**: Build a GUI to make the program more interactive and user-friendly.

## 📜 License

This project is open-source and licensed under the MIT License.
