MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 200,
}

money = {
    "value": 0,
}

def report(resources, money) :
    print(f"Water Left: {resources['water']}")
    print(f"Milk Left: {resources['milk']}")
    print(f"Coffee Left: {resources['coffee']}")
    print(f"Money Made: {money['value']}")

def resource_check(resources, choice) :
    ingredients = MENU[choice]['ingredients']
    for item in ingredients :
        if ingredients[item] > resources[item] :
            print("Sorry Not Enough stock is present\n")
            return False
    return True

def coin_calculate(choice, pennies, nickles, dimes, quaters, money) :
    cost = MENU[choice]['cost']
    total_money = (0.01*pennies) + (0.05*nickles) + (0.10*dimes) + (0.25*quaters)
    if total_money >= cost :
        change = total_money - cost
        print(f"Here's your Change: {change}\n")
        money['value'] += cost
        return True
    else :
        print("Not enough Money\n")
        return False
        
    
def ingridents_check(resources, choice) :
    ingredients = MENU[choice]['ingredients']
    for item in ingredients :
        resources[item] -= ingredients[item]

continue_making = False
while not continue_making :
    choice = input("What you want to drink\nEspresso\nLatte\nCappuccino\n").lower()
    if choice == "report" :
        report(resources, money)
    elif choice in MENU :
        if resource_check(resources, choice) :
            print('Enter the Money\n')
            pennies = int(input("Enter the pennies\n"))
            nickles = int(input("Enter the nickles"))
            dimes = int(input("Enter the dimes\n"))
            quaters = int(input("Enter the quaters\n"))
            if coin_calculate(pennies, nickles, dimes, quaters, money) == True :
                print("Here's Your Coffee Enjoy\n")
                ingridents_check(resources, choice)
    else :
        print("Powering off\n")
        continue_making = True