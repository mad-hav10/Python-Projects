#The Secret Auction Program
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
other_user = True
dic_of_bid = {}

while other_user :
    name = input("Enter the name of the bidder\n")
    bid_price = float(input("Enter the bid ammount you want to bid\n"))
    dic_of_bid[name] = bid_price
    choice = int(input("Enter 1 if there is other person else write 0\n"))

    if choice == 1 :
        print("\n" * 20)

    else :
        other_user = False 
        max_value = max(dic_of_bid.values())
        max_key = max(dic_of_bid.keys())
        print(f"So, the winner of this bid is {max_key}, with highest bid of {max_value}\n")