BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

card = {}
to_learn = {}
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original = pandas.read_csv("french_words.csv")
    to_learn = original.to_dict("records")
else:
    to_learn = data.to_dict(orient="records")


def switchcards():
    global card
    canvas.itemconfig(canvasimage, image=back)
    canvas.itemconfig(french_word, text=card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")


def wrong_fun():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    print(card)
    word = card["French"]
    canvas.itemconfig(french_word, text=word, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(canvasimage, image=front)
    flip_timer = window.after(3000, func=switchcards)


def right_fun():
    to_learn.remove(card)
    word_to = pandas.DataFrame(to_learn)
    word_to.to_csv("words_to_learn.csv", index=False)
    wrong_fun()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)


flip_timer = window.after(3000, func=switchcards)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(
    file="C:\\Users\\PC\\PycharmProjects\\mile-to-km\\100daysofcodeprojects\\flash-card-project-start\\images\\card_front.png")
back = PhotoImage(
    file="C:\\Users\\PC\\PycharmProjects\\mile-to-km\\100daysofcodeprojects\\flash-card-project-start\\images\\card_back.png")
canvasimage = canvas.create_image(10, 10, image=front, anchor=NW)
language = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
french_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(
    file="C:\\Users\\PC\\PycharmProjects\\mile-to-km\\100daysofcodeprojects\\flash-card-project-start\\images\\wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, padx=50, command=wrong_fun)
wrong_button.grid(column=0, row=1)

right = PhotoImage(
    file="C:\\Users\\PC\\PycharmProjects\\mile-to-km\\100daysofcodeprojects\\flash-card-project-start\\images\\right.png")
right_button = Button(image=right, highlightthickness=0, borderwidth=0, padx=50, command=right_fun)
right_button.grid(column=1, row=1)
window.mainloop()
