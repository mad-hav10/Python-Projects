#Treasure Island
print("Welcome to treasure island your motive is to find the treasure\n")
option1 = input("Do you want to go left or right\n").lower()

if option1 == "left" :
    option2 = input("Would you swim or wait\n").lower()

    if option2 == "wait" :
        option3 = input("Which door you choose red, yellow, or blue\n").lower()

        if option3 == "yellow" :
            print("You Win\n")

        else :
            print("You Lose\n")

    else :
        print("You Lose\n")

else :
    print("You Lose\n")
