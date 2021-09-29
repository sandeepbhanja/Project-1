import tkinter
import webbrowser
import time

from tkinter import *

root = Tk()                                                                     #creates a window

root.title("Scientific Calculator")                                             #name of window

root.geometry('1920x1080')                                                      #screen resolution

lbl = Label(text = "Click the button to Start the Calculator:\n")               #write text in a window

lbl.grid()                                                                      #The grid() function is a geometry manager which keeps the label in the desired location inside the window


def click():
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

but = Button(root,text= "Start",fg="red",command = click)

but.grid(column=0,row=1)

root.mainloop()

root.after(5000,lambda:root.destroy())

root1 = Tk()

root1.title("RickRolling Baby")

root1.geometry('350x250')

lbl = Label(text = "Congratulation! You have been RickRolled Sunshine\n")

lbl.grid()

root1.mainloop()                                                                #to run the application
