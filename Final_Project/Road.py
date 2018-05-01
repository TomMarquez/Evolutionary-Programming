"""Class for creating the road
"""

import tkinter as tk
from tkinter import *
import random as rd
import math

class Road(object):
    def __init__(self, canvas, x0, y0, dist_between_roads, Y_SIZE):
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.dist_between_road = dist_between_roads
        self.x1_coords = []
        # Array holds the x, y coords for the first line
        self.xy1_coords = []
        # Array holds the x, y coords for the second line
        self.xy2_coords = []
        self.line1 = []
        self.line2 = []
        # Variable to find 2 other random numbers
        self.rand_diff = 10
        # Var for adding the y value after each iteration
        self.add_y = 10
        self.y_size = Y_SIZE

        self.create_line()
    
    def update_road(self):

        for i in range(3):
            # Next, add new random x based on the x coordinate in the last spot in the array
            # coordinates plus y+6
            x = self.xy1_coords[len(self.xy1_coords) - 2]
            #x = xy_array[0]
            y = self.xy1_coords[len(self.xy1_coords) - 1]

            x = rd.choice([x-self.rand_diff, x, x+self.rand_diff])

            self.xy1_coords.append(x)
            self.xy1_coords.append(y+6)
            self.xy2_coords.append(x+self.dist_between_road)
            self.xy2_coords.append(y+6)

        #self.line1 = self.canvas.create_line(self.xy1_coords, fill="green", smooth="true")
        #self.line2 = self.canvas.create_line(self.xy2_coords, fill="green", smooth="true")
        #self.root.after(1000, self.canvas.update())
        #self.canvas.update()

    def create_line(self):
        # Variable for line two
        line2_var = 100
        while self.y0 < self.y_size:
            x1 = self.x0
            self.x1_coords.append(x1)
            y1 = self.y0
            x2 = x1
            y2 = y1 + self.add_y
            x3 = rd.choice([self.x0-self.rand_diff, self.x0, self.x0+self.rand_diff])
            y3 = y2
            new_x0 = rd.choice([self.x0-self.rand_diff, self.x0, self.x0+self.rand_diff])
            self.x0 = new_x0
            self.xy1_coords.append(self.x0)
            self.xy1_coords.append(self.y0)
            self.xy2_coords.append(self.x0 + line2_var)
            self.xy2_coords.append(self.y0)
            self.y0 += self.add_y
        self.line1 = self.canvas.create_line(self.xy1_coords, fill="green", smooth="true")
        self.line2 = self.canvas.create_line(self.xy2_coords, fill="green", smooth="true")
        #self.canvas.update()

    def line_coords(self):
        """Return 2 arrays of lines to determine if car runs into either side of the road"""
        return self.canvas.coords(self.line1), self.canvas.coords(self.line2)

    def get_x1_coords(self):
        return self.x1_coords

