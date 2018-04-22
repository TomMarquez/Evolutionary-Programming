"""Class for creating the road
"""

import tkinter as tk
from tkinter import *
import random as rd
import math

class Road(object):
    def __init__(self, canvas, x0=350, y0=0):
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.line1 = []
        self.line2 = []

        self.create_line()

    def create_line(self):
        # Array holds the x, y coords for the first line
        xy1_coords = []

        # Array holds the x, y coords for the second line
        xy2_coords = []

        # Variable to find 2 other random numbers
        rand_diff = 6

        # Var for adding the y value after each iteration
        add_y = 6

        # Variable for line two
        line2_var = 100
        while self.y0 < 800:
            x1 = self.x0
            y1 = self.y0
            x2 = x1
            y2 = y1 + add_y
            x3 = rd.choice([self.x0-rand_diff, self.x0, self.x0+rand_diff])
            y3 = y2
            new_x0 = rd.choice([self.x0-rand_diff, self.x0, self.x0+rand_diff])
            self.x0 = new_x0
            xy1_coords.append(self.x0)
            xy1_coords.append(self.y0)
            xy2_coords.append(self.x0 + line2_var)
            xy2_coords.append(self.y0)
            self.y0 += add_y
        self.line1 = self.canvas.create_line(xy1_coords, fill="green", smooth="true")
        self.line2 = self.canvas.create_line(xy2_coords, fill="green", smooth="true")
        #self.canvas.update()

    def line_coords(self):
        """Return 2 arrays of lines to determine if car runs into either side of the road"""
        return self.canvas.coords(self.line1), self.canvas.coords(self.line2)

