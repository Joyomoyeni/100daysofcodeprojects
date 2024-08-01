import os
from blind_auction_art import logo
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.
continu = True
bid ={}
print(logo)
while(continu == True):
    name = input("What is your name: ")
    bidd = int(input("What is your bid: $"))
    bid[name] = bidd
    quest = int(input("Does and other person want to bid, 1 for yes and 2 for no:" ))
    if(quest == 1):
        clear()
        continu = True
    elif(quest == 2):
        continu = False
for n in bid:
    max_bid = 1
    max_per = ""
    if(bid[n] > max_bid):
        max_bid  =bid[n]
        max_per = n
print(f"The highest bid is ${max_bid} from {max_per}.")
