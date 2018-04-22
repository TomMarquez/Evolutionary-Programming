"""Car class

"""

import tkinter as tk
from tkinter import *
import time

WIDTH = 2
OUTLINE = 'gray'
FILL = 'gray'
WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 800

class Car(object):
    def __init__(self, canvas, x0 = 400, y0=700, x1=430, y1=760):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.canvas = canvas
        self.car = canvas.create_rectangle(x0, y0, x1, y1, outline=OUTLINE, fill=FILL, width=WIDTH)

        canvas.pack(fill=BOTH, expand=1)

    def car_update(self):
        """Updates the car position
        Checks to make sure it has not ran out of bounds
        May need to do the checking in the window, since the car will need to know where the road is
        TODO: Currently, this method moves the car to the left. Will need to update it so it moves based on its
        DNA"""
        car_pos = self.canvas.coords(self.car)
        if WINDOW_SIZE_X <= car_pos[0]:
            print("out of Bounds!!")
        time.sleep(0.5)
        x = 50
        y = 0
        self.canvas.move(self.car, x, 0)
        self.canvas.update()

    def car_coords(self):
        """Returns the cars coordinates to test if it has it the wall of the road"""
        return self.canvas.coords(self.car)