from tkinter import *

window = Tk()
window.title("Dollar to Naira Converter")
window.minsize(height=300, width=300)

miles = Label(text="Dollars")
miles.grid(column=2, row=0)

kilo = Label(text="Naira")
kilo.grid(column=2, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

answer = Label(text=0)
answer.grid(column=1, row=1)

user = Entry(width=10)
user.grid(column=1, row=0)


def converter():
    mill = int(user.get())
    kill = round((mill * 1590), 2)
    answer["text"] = kill


button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

window.mainloop()
