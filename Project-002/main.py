#Tip Calculator
def TipCalculator() :
    bill = float(input("Enter the total ammount of bill to be paid\n"))
    tip = float(input("Enter the percent of tip you want to give\n"))
    people = float(input("Enter the no. of people you want to split the bill in\n"))

    bill_after_tip = bill + ((tip/100)*bill)
    splited_bill = bill_after_tip/people
    return[splited_bill]

result = TipCalculator()
print(result)