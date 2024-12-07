#Password Generator
import random

def PasswordGenerator(letter, number, symbol) :
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    while letter != 0 :
        random_letter = random.choice(letters)
        password_list.append(random_letter)
        letter -= 1

    while number != 0 :
        random_number = random.choice(numbers)
        password_list.append(random_number)
        number -= 1

    while symbol != 0 :
        random_symbol = random.choice(symbols)
        password_list.append(random_symbol)
        symbol -= 1

    random.shuffle(password_list)
    result = "".join(password_list)
    print(result)

result2 = PasswordGenerator(2, 5, 3)
print(result2)