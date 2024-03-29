from tkinter import *
import math

# constants

BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# countdown mechanism

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
            check_mark_label.config(text=mark)


# window

window = Tk()
window.title("Pamodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# button functions

def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=BLACK)
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# button

start_button = Button(text="Start", command=start)
start_button.grid(row=3, column=1)
rest_button = Button(text="Reset", command=reset)
rest_button.grid(row=3, column=3)

# label

check_mark_label = Label(text="", bg=YELLOW,font=("Arial", 16, "bold"), fg=GREEN)
check_mark_label.grid(row=4, column=2)
timer_label = Label(text="Timer", font=("Arial", 24, "bold"), bg=YELLOW)
timer_label.grid(row=1, column=2)

window.mainloop()
