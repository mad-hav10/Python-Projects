#The calculator Project
def Addition(num1, num2) :
    return num1 + num2

def Subtraction(num1, num2) :
    return num1 - num2

def Multiplication(num1, num2) :
    return num1 * num2

def Division(num1, num2) :
    return num1 / num2

def Calculation(num1, num2, symbol) :
    if symbol == "+" :
        return Addition(num1, num2)
    elif symbol == "-" :
        return Subtraction(num1, num2)
    elif symbol == "*" :
        return Multiplication(num1, num2)
    else :
        return Division(num1, num2)

have_to_continue = True
while have_to_continue :

    want_to_continue = True
    operation = ['+', '-', '*', '/']
    num1 = float(input("Enter the 1st num\n"))
    while want_to_continue :
    
        for i in operation :
            print(i)

        symbol = input('Enter the operation you want to perform\n')

        num2 = float(input("Enter the 2nd num\n"))

        result = Calculation(num1, num2, symbol)
        print(f"{num1} {symbol} {num2} = {result}")
        num1 = result

        choice = input(f"Press 1 if you want to further calculate {result}, or press 0 to start a new calculation\n")

        if choice == "0" :
            want_to_continue = False
            print("\n" * 20)