from tkinter import Tk, Canvas, PhotoImage, Label, Button

from numpy.core.defchararray import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick = "✔"
reps = 0
tim = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps
    window.after_cancel(tim)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def startfun():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def count_down(count):
    global tim
    minu = int(count / 60)
    sec = (count % 60)
    if minu < 10:
        minu = "0" + str(minu)
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text=f"{minu}:{sec}")
    if count > 0:
        tim = window.after(1000, count_down, count - 1)
    else:
        startfun()
        mark = ""
        sessions = int(reps / 2)
        for n in range(sessions):
            mark += tick
        check.config(text=mark)


timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

start = Button(text="Start", highlightthickness=0, command=startfun)
start.grid(column=0, row=2)

reseet = Button(text="Reset", highlightthickness=0, command=reset_time)
reseet.grid(column=2, row=2)

photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
