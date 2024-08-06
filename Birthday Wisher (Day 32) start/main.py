import smtplib


myemail = "folakemijoy492@gmail.com"
import datetime as dt
import random


now = dt.datetime.now()
day = now.weekday()

quotes_list = []
with open("quotes.txt", "r") as quotes:
    quotes_list = [line[:-1] for line in quotes]

def mondayquote():
    quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myemail, password="xrqnrctvneuzkdwv")
        connection.sendmail(from_addr=myemail, to_addrs=myemail,
                            msg=f"Subject:Hello\n\n{quote}")

if day == 4:
    mondayquote()
