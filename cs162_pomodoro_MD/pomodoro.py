## Github link
##






import tkinter as tk

YELLOW = "#DADBBD"          #color
FONT = "Courier"
STUDY_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 15
intervals = 0
timer = None

# Homework for this week
# Expand on this app, make it your own!
# Extra fun: make an image with tkinter and post your image on Discord

#Challenge: change the text



## -- Adding Functions --

def next_timer():
    """Go to next interval."""
    global intervals

    next_button["state"] = "disabled"
    # Pause the counting down
    pause_timer()

    #configure the canvas text to "00:00"
    canvas.itemconfig(timer_text, text = "00:00")
    intervals += 1


def pause_timer():
    global timer
    pause_button["state"] = "disabled"
    start_button["state"] = "active"

    if timer:
        window.after_cancel(timer)
        timer = None


def count_down(count):
    global timer
    # what if we want to count from 5 mins?   
    # 5 * 60 == 300
    count_mins = count // 60 ##floor division
    count_secs = count % 60  ## modulus division
    #canvas.itemconfig(timer_text, text=count)  #00:00 -> 5
    if count_secs < 10:  #modify the format from 9 to 09, once seconds is smaller than 10
        count_secs = f"{count_secs:02d}"  # 4:09, not 4:9 #checkout python f-string documentation
    if count_mins < 10:
        count_mins = f"{count_mins:02d}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}") #5:00, not 5:0
    ## see docs on [after] method below
    ## https://tcl.tk/man/tcl8.6/TclCmd/after.htm
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  #5 - 1


## Start the timer
def start_timer():
    global intervals

    # print(start_button["text"])
    start_button["state"] = "disabled"
    pause_button["state"] = "active"
    next_button["state"] = "active"

    study_sec = STUDY_TIME * 60
    short_break = SHORT_BREAK * 60
    long_break = LONG_BREAK * 60

    intervals += 1
    print(intervals)

## Challenge for me:
# 1) 25 min (study)
# 2) 5 min (break)
# 3) 25 min study
# 4) 5 min short break
# 5) 25 min study
# 6) 5 min short break
# 7) 25 min (this is already the 4th round of studying)
# 8) 15min LONG BREAK


    ## Thinking process:
    ## HINT: % operator might be helpful here.
    ## if it's the 1), 3), 5), 7) intervals
    ## count_down(study_sec)
    ## if it's the 8) interval
    ## count_down(long_break)
    ## if it's the 2), 4), 6) intervals

    ## if the pause button is active, and if not "00:00"
    ##                                  position: 01234
    ## get that current time, and pass that current time to count_down() again
    ## count_down(current_time)

    current_timer = canvas.itemcget(timer_text, "text")
    if current_timer != "00:00" and pause_button["state"] == "active":
        # print(current_timer)
        # print(type(current_timer)) 15:56
        # using string slice and type casting to get timer_text and convert to integer to resume timer at stop
        current_timer = int(current_timer[0:2]) * 60 + int(current_timer[3:])
        # current_time = 15 * 60 + 56
        # reassign to current timer and count down again.
        count_down(current_timer)

    elif intervals % 8 == 0:
        count_down(long_break)
    elif intervals % 2 == 0:
        count_down(short_break)
    else:
        count_down(study_sec)

    ##count_down(300) ## quick test


## -- Setting UP Our GUI --

window = tk.Tk()
window.title("Pomodoro")
# window.minsize(width=600,height=650)
window.config(padx=50,pady=50,bg=YELLOW)

canvas = tk.Canvas(width=600, height=650, bg=YELLOW) #highlightthickness = 0  "gets rid of border"
#Place image on canvas
tomato_img = tk.PhotoImage(file="tomato_character.png")     #img dimensions: 455 x 601
canvas.create_image(315, 320, image=tomato_img)  #not keyword arg (for ex: 'width=' or 'height='), but instead positional arguments
    #in create image we cannot use the image directly, must set the image to a variable.
timer_text = canvas.create_text(315, 400, text="00:00", fill="white" ,font=(FONT, 55, "bold"))

#create text on top of the image

canvas.grid(column=1, row=1)

## Trying out the count_down() starting from 5?
##count_down(5)


## Try out counting down from 5 and see if the timer_text [00:00] get updated?
# import time

# count = 5
# while count>0:
#     time.sleep(1)
#     count -= 1
#     canvas.itemconfig(timer_text, text=f"{count}")

interval_label = tk.Label(text="TIMER", bg=YELLOW, font=(FONT,50, "bold"))
interval_label.grid(column=1,row=0)

start_button = tk.Button(text="START", width=10, height=2, bd=10, bg="#D82148", command = start_timer)
start_button.grid(column=0,row=2)

pause_button = tk.Button(text="PAUSE/RESET", width=10, height=2, bd=10, bg="#D82148", command = pause_timer) ##command
pause_button.grid(column=1,row=2)

next_button = tk.Button(text="next", width=10, height=2, bd=10, bg="#D82148", command = next_timer)
next_button.grid(column=2,row=2)

window.mainloop()
