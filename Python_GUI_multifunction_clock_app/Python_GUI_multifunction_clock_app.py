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
ttk.Label(TAB2, text="Alarm clock - No widgets yet!").grid(column=0, row=0, padx=10, pady=10)

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
ttk.Label(TAB4, text="Stopwatch - No widgets yet!").grid(column=0, row=0, padx=10, pady=10)

#About code
ttk.Label(TAB5, text="\nThis app is created as part of Python programming self study.\n\nCreator: Michal Kala\n\nCheck my github profile:\n").grid(column=0, row=0)

def github_open():
    webbrowser.open_new(r"https://github.com/MichalKala")

link = ttk.Button(TAB5, text="GITHUB", command=github_open)
link.grid(row=1, column=0)

TAB_CONTROL.pack(expand=1, fill="both")
#Display the window until you close it
gui.mainloop()



