import datetime as dt
import pandas
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

items = []
with open(r"C:\Users\sodiu\OneDrive\Documents\Coding\Python Projects\Project-022\quotes.txt", "r") as quotes :
    for lines in quotes :
        items.append(lines.strip())

random_quote = random.choice(items)

if weekday == 2 :
    my_email = "python.madhav.practice@gmail.com"
    my_password = "morayjtpvoerpaet"
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= "madhavlalit04@gmail.com",
            msg= f"Subject:Today's Quote\n\n{random_quote}")