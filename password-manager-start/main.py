from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    pass_letter = [random.choice(letters) for n in range(0, nr_letters)]
    pass_number = [random.choice(numbers) for o in range(0, nr_numbers)]
    pass_symbol = [random.choice(symbols) for p in range(0, nr_symbols)]
    pass_list = pass_number + pass_letter + pass_symbol
    random.shuffle(pass_list)
    passw = "".join(pass_list)
    password.insert(0, passw)
    pyperclip.copy(passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    newdata = {website.get():
                   {
                       "email": email.get(),
                       "password": password.get()
                   }}
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showerror(title="Missing details", message="You have not filled in some important information.")
    else:
        try:
            with open("password.json", "r") as file:
                daa = json.load(file)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(newdata, file, indent=4)
        else:
            daa.update(newdata)

            with open("password.json", "w") as file:
                json.dump(daa, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)

def look_pass():
    webs = website.get()
    with open("password.json", "r") as file:
        dict = json.load(file)
    pasw = dict[webs]["password"]
    emai = dict[webs]["email"]
    messagebox.showinfo(title=webs, message=f"Email:{emai}\nPassword:{pasw}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website = Entry(width=17, justify="left")
website.grid(column=1, row=1)
window.focus()

searh = Button(text="Search", bg="blue", fg="white", command=look_pass)
searh.grid(column=2, row=1)

email = Entry(width=35, justify="left")
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "folakemijoy492@gmail.com")

password = Entry(width=17)
password.grid(column=1, row=3)

generate = Button(text="Generate Password", justify="left", command=gen_pass)
generate.grid(column=2, row=3)

add = Button(text="Add", command=save_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
