from tkinter import *
import math
# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25#well you can change acordingly
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer=None
#timer mechanism
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0

def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps % 8==0:
        countdown(long_break_sec)
        title_label.config(text="BREAK",fg=RED)
    elif reps% 2==0:
        countdown(short_break_sec)
        title_label.config(text="BREAK",fg=PINK)

    else:
        countdown(work_sec)
        title_label.config(text="BREAK",fg=GREEN)
 


#countdownmechanism
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_sec==0:
        count_sec="00"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✓"
        check_marks.config(text=mark)    
# UI Setup
window = Tk()
window.title("Pomodoro ")
window.configure(padx=100, pady=50, bg=YELLOW)



title_label = Label(text="Timer", fg=GREEN,bg=YELLOW,font=(FONT_NAME,30))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 125, image=tomato_img)
timer_text=canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)  # Moved canvas to row 1

start_button=Button(text="START",highlightthickness=0,bg=GREEN,fg="white",command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="RESET",highlightthickness=0,bg=GREEN,fg="white",command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME, 20))
check_marks.grid(column=1,row=3)
window.mainloop()
