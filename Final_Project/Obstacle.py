"""Obstacle Class

"""

import tkinter as tk
from tkinter import *
import random

class Obstacle(object):
    def __init__(self, canvas, size, x, y, road_array, road_distance):
        self.canvas = canvas
        self.size = size
        self.x = y
        self.y = x
        #self.y = y
        self.canvas = canvas
        self.obstacle = canvas.create_rectangle(self.x, self.y, self.x+size, self.y+size, width=size)
        self.element = 0

    def get_x_y_coords(self,road1_array, road_distance):
        rand_elem = random.randrange(len(road1_array))
        if rand_elem % 2 != 0 and rand_elem != len(road1_array):
            rand_elem + 1
        elif rand_elem % 2 != 0 and rand_elem != 0:
            rand_elem - 1
        y = rand_elem * 5
        x = random.randrange(road1_array[rand_elem], road1_array[rand_elem] + road_distance)
        self.element = rand_elem
        return x, y

    def obstacle_coords(self):
        """Return 2 arrays of lines to determine if car runs into either side of the road"""
        return self.x, self.element
        #return self.canvas.coords(self.obstacle)