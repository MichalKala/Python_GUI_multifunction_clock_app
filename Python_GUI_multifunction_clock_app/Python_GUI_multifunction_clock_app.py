from tkinter import Tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sys
import time
import datetime
import webbrowser


#Create basic window
gui = Tk()
gui.title("Michal's multi-function clock app")
gui.geometry('540x360')

#Create Tabs
TAB_CONTROL = ttk.Notebook(gui)

#Tab1 - Current time
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Current time')

#Tab2 - Alarm clock
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Alarm clock')

#Tab3 - Countdown timer
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Countdown timer')

#Tab4 - Stopwatch
TAB4 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB4, text='Stopwatch')

#Tab4 - About
TAB5 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB5, text='About')

#Current Time code
ttk.Label(TAB1, font=("times", 18), text="Current time: ").grid(column=0, row=0, sticky=W, padx=5, pady=5)

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


clock=ttk.Label(TAB1, font=("times", 18, "bold"))
clock.grid(row=1, column=0, sticky=W, padx=5, pady=5)
tick()

ttk.Label(TAB1, font=("times", 18), text="Date: ").grid(column=0, row=2, sticky=W, padx=5, pady=5)
today = datetime.date.today()
datum = ttk.Label(TAB1, font=("times", 18, "bold"), text=today).grid(column=0, row=3, sticky=W, padx=5, pady=5)

image = PhotoImage(file="date_time.png")
obrazek = ttk.Label(TAB1, image=image).grid(column=2, row=0, columnspan=2, rowspan=4, sticky=W+E+N+S, padx=10, pady=10)


#Alarm Clock code
ttk.Label(TAB2, font=("times", 12), text="Current time: ").grid(column=0, row=0, sticky=W, padx=5, pady=5)

def tick2():
    time_string = time.strftime("%H:%M:%S")
    clock2.config(text=time_string)
    clock2.after(200, tick2)


clock2=ttk.Label(TAB2, font=("times", 12, "bold"))
clock2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
tick2()

ttk.Label(TAB2, font=("times", 12), text="Choose amount of time after which I wake you up: ").grid(column=0, columnspan=2, row=2, padx=5, pady=5)
ttk.Label(TAB2, text="Hours:").grid(column=0, row=3, padx=10, pady=10, sticky=W)
entry2 = ttk.Entry(TAB2, width = 5, font = 'Calibri 10')
entry2.grid(column=1, row=3, padx=10, pady=10)

ttk.Label(TAB2, text="Minutes:").grid(column=0, row=4, padx=10, pady=10, sticky=W)
entry3 = ttk.Entry(TAB2, width = 5, font = 'Calibri 10')
entry3.grid(column=1, row=4, padx=10, pady=10)

alarm_clock=ttk.Label(TAB2, font=("times", 35, "bold"), text=str(datetime.timedelta(seconds=0)))
alarm_clock.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def alarm_countdown(alarm_count):
    # change text in label        
    alarm_clock['text'] = str(datetime.timedelta(seconds=alarm_count))

    if alarm_count > 0:
        # call countdown again after 1000ms (1s)
        gui.after(1000, alarm_countdown, alarm_count-1)
    if alarm_count == 0:
        alarm_clock['foreground'] = "red"
        webbrowser.open_new(r"https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def setbutton_handle():
    hours_collector = entry2.get()
    minutes_collector = entry3.get()
    hours_collector = int(hours_collector)
    minutes_collector = int(minutes_collector)
    ttk.Label(TAB2, font=("times", 12), text="OK I will wake you up in %d hours and %d minutes." % (hours_collector, minutes_collector)).grid(column=0, row=5, columnspan=2, padx=10, pady=10)
    alarm_result = hours_collector * 3600 + minutes_collector * 60
    alarm_countdown(alarm_result)

setbutton = ttk.Button(TAB2, text="Set", command=setbutton_handle)
setbutton.grid(column=2, row=4, padx=10, pady=10)

#Countdown timer code
ttk.Label(TAB3, text="Set the time in seconds and press GO:").grid(column=0, row=0, padx=10, pady=10)
entry1 = ttk.Entry(TAB3, width = 5, font = 'Calibri 10')
entry1.grid(column=1, row=0, padx=10, pady=10)
countdown_clock=ttk.Label(TAB3, font=("times", 50, "bold"), text=str(datetime.timedelta(seconds=0)))
countdown_clock.grid(row=2, column=0, padx=10, pady=10)

def countdown(count):
    # change text in label        
    countdown_clock['text'] = str(datetime.timedelta(seconds=count))

    if count > 0:
        # call countdown again after 1000ms (1s)
        gui.after(1000, countdown, count-1)
    if count == 0:
        countdown_clock['foreground'] = "red"



def gobutton_handle():
    counter = entry1.get()
    counter = int(counter)
    ttk.Label(TAB3, text="You have entered the amount of %d seconds." % counter).grid(column=0, row=1, padx=10, pady=10)
    countdown(counter)

gobutton = ttk.Button(TAB3, text="GO", command=gobutton_handle)
gobutton.grid(column=2, row=0, padx=10, pady=10)



#Stopwatch code

stopwatch_clock=ttk.Label(TAB4, font=("times", 50, "bold"), text=str(datetime.timedelta(seconds=0)))
stopwatch_clock.grid(row=1, column=0, columnspan=4, rowspan=1, padx=10, pady=10)
stopwatch_running = False
def start_button_function(start_count):

    if stopwatch_running:
    
        stopwatch_clock['text'] = str(datetime.timedelta(seconds=start_count))

        if start_count > 0:
        
            gui.after(1000, start_button_function, start_count+1)

def start_button_handle():
    global stopwatch_running
    stopwatch_running = True
    start_button_function(1)

start_button = ttk.Button(TAB4, text="START", command=start_button_handle)
start_button.grid(column=0, row=2, padx=10, pady=10)

def stop_button_handle():
    global stopwatch_running
    stopwatch_running = False

stop_button = ttk.Button(TAB4, text="STOP", command=stop_button_handle)
stop_button.grid(column=1, row=2, padx=10, pady=10)

def reset_button_handle():
    stopwatch_clock['text'] = str(datetime.timedelta(0))
    global stopwatch_running
    stopwatch_running = False

reset_button = ttk.Button(TAB4, text="RESET", command=reset_button_handle)
reset_button.grid(column=2, row=2, padx=10, pady=10)

#About code
ttk.Label(TAB5, text="\nThis app is created as part of Python programming self study.\n\nCreator: Michal Kala\n\nCheck my github profile:\n").grid(column=0, row=0)

def github_open():
    webbrowser.open_new(r"https://github.com/MichalKala")

link = ttk.Button(TAB5, text="GITHUB", command=github_open)
link.grid(row=1, column=0)

TAB_CONTROL.pack(expand=1, fill="both")
#Display the window until you close it
gui.mainloop()



