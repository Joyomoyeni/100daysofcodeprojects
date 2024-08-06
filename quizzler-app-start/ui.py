import time

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.scorelabel = Label(text="Score:0", background=THEME_COLOR, foreground="white")
        self.scorelabel.grid(column=1, row=0)

        self.canvas = Canvas(self.window, width=300, height=250, highlightthickness=0, bg="white")
        self.quest = self.canvas.create_text(150, 125, font=("Arial", 10, "italic"), text="Some question text",
                                             fill=THEME_COLOR, width=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.wrongimg = PhotoImage(
            file="C:\\Users\\PC\\PycharmProjects\\mile-to-km\\100daysofcodeprojects\\quizzler-app-start\\images\\false.png")
        self.wrong = Button(image=self.wrongimg, highlightthickness=0, command=self.noo)
        self.wrong.grid(row=2, column=1)
        self.rightimg = PhotoImage(
            file="C:\\Users\\PC\\PycharmProjects\\mile-to-km\\100daysofcodeprojects\\quizzler-app-start\\images\\true.png")
        self.right = Button(image=self.rightimg, highlightthickness=0, command=self.tick)
        self.right.grid(row=2, column=0)

        self.nextquest()
        self.window.mainloop()

    def nextquest(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scorelabel.config(text=f"Score : {self.quiz.score}")
            qtext = self.quiz.next_question()
            self.canvas.itemconfig(self.quest, text=qtext)
        else:
            self.canvas.itemconfig(self.quest, text="You've run out of questions.")
            self.wrong.config(state="disabled")
            self.right.config(state="disabled")

    def tick(self):
        vale = self.quiz.check_answer("True")
        self.givefeed(vale)

    def noo(self):
        valu = self.quiz.check_answer("False")
        self.givefeed(valu)

    def givefeed(self, val):
        if val:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.nextquest)

