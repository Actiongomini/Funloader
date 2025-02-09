import os
import tkinter
from tkinter import *

#variables
dir_path = os.path.dirname(os.path.realpath(__file__))
text="funloader v0.1"
mom = tkinter.Tk()
mom.overrideredirect(1)
mom.withdraw()

#dictionaries
game_path = {'quarantine':"fun-ctions\\mvolution\\quarantine\\site.html",
             'we_need_to_talk':"fun-ctions\\dodoot\\we-need-to-talk\\site.html",
             'chrome_dino':"fun-ctions\\yolwoocle\\pico-dino\\site.html",
             'eaglercraft':"fun-ctions\\eaglercraft\\main.html",
             'intertwine':"fun-ctions\\crescence-studio\\intertwine\\site.html",
             }
#functions
def messagewindow(): #main option menu
    win = Tk()
    win.title(text)
    message = "What fun-ction would you like"
    
    screen_width = win.winfo_screenwidth() #get screen measurements
    screen_height = win.winfo_screenheight()
    window_width = 170  # Adjust when needed
    window_height = 200

    x_position = (screen_width - window_width) // 2 #find centre window
    y_position = (screen_height - window_height) // 2

    win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}") #move window
    
    Label(win, text=message).pack()
    
    #game buttons
    Button(win, text='Eaglercraft', command=lambda: run('eaglercraft')).pack()
    Button(win, text='Quarantine', command=lambda: run('quarantine')).pack()
    Button(win, text='We need to talk', command=lambda: run('we_need_to_talk')).pack()
    Button(win, text='Chrome Dino', command=lambda: run('chrome_dino')()).pack()
    Button(win, text='Intertwine', command=lambda:run('intertwine')).pack()

    Button(win, text='Quit', command=lambda: quit()).pack()

def run(game):
    file_path = os.path.join(dir_path,game_path[game])
    os.startfile(file_path)

#start
os.chdir(dir_path)
messagewindow()
mom.mainloop()

#how to add a new game
# 1. Add the game to the fun-ctions folder
# 2. Add the game to the dictionary game_path
# 3. Add a button to the messagewindow function
# 4. Your done (might need to adjust the window size)