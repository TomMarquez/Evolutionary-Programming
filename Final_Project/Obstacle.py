"""Obstacle Class

"""

import tkinter as tk
from tkinter import *
import random

class Obstacle(object):
    def __init__(self, canvas, size=10, x=0, y=0):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.canvas = canvas
        self.car = canvas.create_rectangle(self.x, self.y, self.x+size, self.y+size, width=size)

    def get_x_y_coords(self,road1_array, road2_array):
            rand_elem = random.randrange(len(road1_array))
            print(rand_elem)
    