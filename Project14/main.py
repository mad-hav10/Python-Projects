from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_resources = CoffeeMaker()
money_maker = MoneyMachine()
menu = Menu()

is_on = True

while is_on :
    options = menu.get_items()
    choice = input(f"What would you like: {options}\n")
    if choice == "off" :
        is_on = False
    elif choice == "report" :
        coffee_resources.report()
        money_maker.report()
    else :
        drink = menu.find_drink(choice)
        if coffee_resources.is_resource_sufficient(drink) and money_maker.make_payment(drink.cost) :
            coffee_resources.make_coffee(drink)