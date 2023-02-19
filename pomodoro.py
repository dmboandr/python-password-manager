import tkinter
import math

# ------------------------ CONSTANTS ---------------- #
# colorhunt.co
PINK = "#FFCEFE"
RED = "#F55050"
GREEN = "#03C988"
YELLOW = "#FFFBAC"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
FONT_NAME = "Courier"
reps = 0
timer = None


# -------------------------- RESET -------------------------- #
def reset_timer():
    if timer != None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="BLACK")
    check_marks.config(text="")
    global reps
    reps = 0

# ------------------------- TIMER MECHANISM -----------------#
# 25 5 25 5 25 5 25 20 25 5 25 5 ....

def start_timer():
    global reps
    reps += 1

    # функция countdown принимает значение в секундах
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # это каждый восьмой проход
        countdown(long_break_sec)
        title_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        # это каждый второй проход
        countdown(short_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

#-------------------------- COUNTDOWN MECHANISM --------------#

def countdown(count):
    count_min = math.floor(count//60)  # 100 // 60 = 1
    count_sec = count % 60  # 100 % 60 = 40

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(100, countdown, count-1)
    else:
        start_timer()
        marks = ""
        works_session = math.floor(reps/2)
        for _ in range(works_session):
            marks += "✓"
        check_marks.config(text=marks)


# ------------------------- GUI ---------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
# padding x, padding y
window.config(padx=2, pady=2, bg=YELLOW)
title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=206, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 113, image=tomato_img)
timer_text = canvas.create_text(100, 130, fill=PINK, text="00:00", font=(FONT_NAME, 40))

canvas.grid(row=1, column=1)
"✓"
# timer_label = tkinter.Label(text="00:00", font=(FONT_NAME, 35))
# timer_label.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = tkinter.Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check_marks.grid(row=2, column=1)

window.mainloop()
