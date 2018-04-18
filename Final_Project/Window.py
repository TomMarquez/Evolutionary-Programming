'''
Window Class

This will provide the window for displaying the simulation

'''

import tkinter as tk
from tkinter import *

# Class for creating the window
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Autonomous Vehicle")

        # allow widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # canvas widget
        canvas = Canvas(self)

        # create a button
        quitButton = Button(self, text="Quit", command=self.client_exit)

        # place button on the window
        quitButton.place(x=0, y=0)

        # create a ractangle (placeholder for car)
        # parameters for rectangle: (x0, y0, x1, y1, option, ...)
        canvas.create_rectangle(400, 600, 430, 660, outline="gray", fill="gray", width=2)

        canvas.pack(fill=BOTH, expand=1)

    def client_exit(self):
        exit()

def main():

    # root window
    root = Tk()
    root.geometry("800x800")
    # create instance
    app = Window(root)

    # main loop
    root.mainloop()

if __name__=='__main__':
    main()