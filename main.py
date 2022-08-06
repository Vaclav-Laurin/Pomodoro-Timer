import datetime
import smtplib
import time
from tkinter import *
from tkinter import messagebox


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FC8A82"
RED = "#e7305b"
GREEN = "#9bdeac"
PASTEL_GREEN = "#09CE72"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
TITLE_FONT = {"name": "Courier", "size": 24, "type": "bold"}
TIMER_FONT = {"name": "Courier", "size": 18, "type": "bold"}
REGULAR_FONT = {"name": "Courier", "size": 12, "type": "normal"}

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

PROGRAM_NAME = "Pomodoro Timer"
IMAGE_PATH = "tomato.png"

CANVAS_SIZE = {"height": 224, "width": 200}
TITLE_PADDING = 25
WINDOW_PADDING = {'x': 50, 'y': 30}

is_Timer_On = False
total_seconds = 0


# ---------------------------- TIMER FUNCTIONS ------------------------------- #
def start_timer():
    global is_Timer_On, total_seconds, start_button

    start_button["state"] = DISABLED
    is_Timer_On = True
    minutes = 0
    seconds = 0
    counter = 0
        
    while True:
        for minute in range(WORK_MIN):
            minutes = minute
            
            for second in range(60):
                if is_Timer_On == False:
                    return
                
                total_seconds += 1
                seconds = second
                new_text = "{:02d}:{:02d}".format(minutes, seconds)
                pomodoro_canvas.itemconfig(pomodoro_text, text=new_text)
                window.update()
                time.sleep(1)
        
        counter += 1
        check_mark_label = Label(master=check_mark_frame, text="✔", fg=GREEN, bg=YELLOW, font=(TITLE_FONT["name"], TITLE_FONT["size"], TITLE_FONT["type"]))
        check_mark_label.pack(side="left")
        
        if counter >= 4 and counter % 4 == 0:
            for minute in range(LONG_BREAK_MIN-1, -1, -1):
                minutes = minute
                
                for second in range(59, -1, -1):
                    if is_Timer_On == False:
                        return
                    seconds = second
                    new_text = "{:02d}:{:02d}".format(minutes, seconds)
                    pomodoro_canvas.itemconfig(pomodoro_text, text=new_text)
                    window.update()
                    time.sleep(1)
        else:    
            for minute in range(SHORT_BREAK_MIN-1, -1, -1):
                minutes = minute
                
                for second in range(59, -1, -1):
                    seconds = second
                    new_text = "{:02d}:{:02d}".format(minutes, seconds)
                    pomodoro_canvas.itemconfig(pomodoro_text, text=new_text)
                    window.update()
                    time.sleep(1)

            
def stop_timer():
    global is_Timer_On, total_seconds
    is_Timer_On = False

    total_minutes = total_seconds//60
    total_hours = total_minutes//60
    
    
    total_time = datetime.time(total_hours, total_minutes, total_seconds)

    messagebox.showinfo("Total Time", f"Your total working time: {total_time} ")

                    
def reset_timer():
    global total_seconds, last_time, start_button
    
    stop_timer()
    
    start_button["state"] = NORMAL
    total_seconds = 0
    
    pomodoro_canvas.itemconfigure(pomodoro_text, text="00:00")
    
    for widget in check_mark_frame.winfo_children():
        widget.destroy()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(PROGRAM_NAME[:8])
window.minsize(height=CANVAS_SIZE["height"]*2, width=CANVAS_SIZE["width"]*2)
window.configure(bg=YELLOW, padx=WINDOW_PADDING['x'], pady=WINDOW_PADDING['y'])

title = Label(text=PROGRAM_NAME,fg=GREEN, bg=YELLOW, font=(TITLE_FONT["name"], TITLE_FONT["size"], TITLE_FONT["type"]), pady=TITLE_PADDING)
title.grid(row=0, column=0, columnspan=2)

pomodoro_canvas = Canvas(height=CANVAS_SIZE["height"], width=CANVAS_SIZE["width"], highlightthickness = 0, bg=YELLOW)
pomodoro_image = PhotoImage(file=IMAGE_PATH)
pomodoro_canvas.create_image(CANVAS_SIZE["width"]/2, CANVAS_SIZE["height"]/2, image=pomodoro_image)
pomodoro_text = pomodoro_canvas.create_text(100, 130, text="00:00", font=(TIMER_FONT["name"], TIMER_FONT["size"], TIMER_FONT["type"]), fill=WHITE)
pomodoro_canvas.grid(row=1, column=0, columnspan=2)

check_mark_frame = Frame(window, height=50, bg=YELLOW)
check_mark_frame.grid(row=2, column=0, columnspan=2)

start_button = Button(text="Start", bg=WHITE, font=(REGULAR_FONT["name"], REGULAR_FONT["size"], REGULAR_FONT["type"]), command=start_timer, highlightthickness=1.5, highlightbackground=PASTEL_GREEN)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", bg=WHITE, font=(REGULAR_FONT["name"], REGULAR_FONT["size"], REGULAR_FONT["type"]), command=reset_timer, highlightthickness=1.5, highlightbackground=PASTEL_GREEN)
reset_button.grid(row=3, column=1)

window.mainloop()