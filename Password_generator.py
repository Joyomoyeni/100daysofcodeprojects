#Password Generator Project
import random
import string_utils
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter = ""
for n in range(0, nr_letters):
    ran = random.randint(0, (len(letters) - 1))
    letter = letter + letters[ran]

symb = ""
for n in range(0, nr_symbols):
    rand = random.randint(0, (len(symbols) - 1))
    symb = symb + symbols[rand]


num = ""
for n in range(0, nr_numbers):
    randm = random.randint(0, (len(numbers) - 1))
    num = num + numbers[randm]
easy = letter + symb + num
print(easy)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(string_utils.shuffle(easy))
