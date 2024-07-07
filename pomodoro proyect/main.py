from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
tiempo=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(tiempo)
    global reps
    reps=0
    timer.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    checkmark.config(text="")

    
   


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starter_time():
    global reps
    reps+=1
    work=25*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if reps%8==0:
        countdown(long_break)
        timer.config(text="Break",fg=RED)

    if reps%2==0 :
        countdown(short_break)
        timer.config(text="Break",fg=PINK)

    else:
        countdown(work)
        timer.config(text="Work")
    
    



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    count_min= math.floor(count / 60)
    count_seg= count % 60
    if count_seg<10:
        count_seg=f"0{count_seg}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_seg}")
    if count>0:
        global tiempo
        tiempo=window.after(1000,countdown,count-1)

    else:
        starter_time()
        mark=""
        if reps%2==0:
            mark+="✔"
        checkmark.config(text=mark)


print(reps)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)

start=Button(text="Start",command=starter_time)
start.grid(column=0,row=2)

timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="python/pomodoro proyect/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


checkmark=Label(text="" ,fg=GREEN , bg=YELLOW)
checkmark.grid(column=1,row=3)


reset=Button(text="Reset",command=reset)
reset.grid(column=2,row=2)






window.mainloop()