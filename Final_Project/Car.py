"""Car class

"""

import tkinter as tk
from tkinter import *
import time
import random

WIDTH = 2
OUTLINE = 'gray'
FILL = 'gray'
WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 800

CAR_LENGTH = 20
CAR_WIDTH = 30

class Car(object):
    def __init__(self, canvas, x0 = 400, y0=0, x1=430, y1=CAR_LENGTH):
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

        moves = []
        for i in range(50):
            moves.append(random.randrange(1))

        car_pos = self.canvas.coords(self.car)
        if WINDOW_SIZE_X <= car_pos[0]:
            print("out of Bounds!!")
        time.sleep(0.5)

        xmove = 5
        ymove = 5

        for i in range(len(moves)):
            self.y0 = self.y0+ymove
            if moves[i] == 0:
                print(self.x0)
                print(self.y0)
                self.x0 = self.x0-xmove
                self.canvas.move(self.car, self.x0, self.y0)
            else:
                self.x0 = self.x0 + xmove
                self.canvas.move(self.car, self.x0, self.y0)
            self.canvas.update()
            time.sleep(0.5)

    def car_coords(self):
        """Returns the cars coordinates to test if it has it the wall of the road"""
        return self.canvas.coords(self.car)

    def crash(self, road):
        #if car_coords() == 0
        return True