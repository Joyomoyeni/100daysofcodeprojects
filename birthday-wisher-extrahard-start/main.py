##################### Extra Hard Starting Project ######################
import datetime

import pandas
import smtplib
import random

# 1. Update the birthdays.csv
birth = pandas.read_csv("birthdays.csv")
print(birth)
month_list = birth["month"].to_list()
name_list = birth["name"].to_list()
mail_list = birth["email"].to_list()
day_list = birth["day"].to_list()

with open("letter_1.txt", "r") as letter:
    letter1 = letter.read()

with open("letter_2.txt", "r") as letter:
    letter2 = letter.read()

with open("letter_3.txt", "r") as letter:
    letter3 = letter.read()
letter_list =[letter1, letter2, letter3]
today = datetime.datetime.now()
today_date = today.day
today_month = today.month
myemail = "folakemijoy492@gmail.com"

# 2. Check if today matches a birthday in the birthdays.csv
if today_date in day_list:
    number = day_list.index(today_date)
    if today_month == month_list[number]:
        letter_of_day = random.choice(letter_list)
        lett = letter_of_day.replace("[NAME]", name_list[number])
        print(lett)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myemail, password="xrqnrctvneuzkdwv")
            connection.sendmail(from_addr=myemail, to_addrs=mail_list[number],
                                msg=f"Subject:Happy birthday\n\n{lett}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
