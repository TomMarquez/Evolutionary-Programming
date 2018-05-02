"""Car class

"""

import tkinter as tk
from tkinter import *
import time
import random

WIDTH = 2
OUTLINE = 'gray'
FILL = 'gray'
WINDOW_SIZE_X = 700
WINDOW_SIZE_Y = 700

class Car(object):
    def __init__(self, canvas, x0=0, y0=0, car_width=0, y1=0, text=""):
        self.x0 = x0
        self.y0 = y0
        self.car_width = car_width
        self.x1 = x0 + car_width
        self.y1 = y1
        self.car_length = y1
        self.canvas = canvas
        self.car = canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=OUTLINE, fill=FILL, width=WIDTH)
        self.text = canvas.create_text(self.x0+car_width/2, self.y0, text=text)
        canvas.pack(fill=BOTH, expand=1)    

    def car_update(self, road1_arr, road2_arr, ROAD_DISTANCE, move):
        """Updates the car position
        Checks to make sure it has not hit the side of the road
        or hit an object
        DNA"""

        moves = []
        moves_size = len(road1_arr)
        # Moves =
        for i in range(moves_size):
            moves.append(random.randrange(3))

        car_pos = self.canvas.coords(self.car)
        #if WINDOW_SIZE_X <= car_pos[0]:
         #   print("out of Bounds!!")

        xmove = self.car_width
        ymove = 10
        #for i in range(len(moves)):
        # if car made it to the end of the road, sto

        #if random number is 0, go stright
        if move == 0 and self.x0 != 0:
            self.x0 = self.x0-xmove
            
            self.canvas.move(self.car, 0, ymove)
            self.canvas.move(self.text, 0, ymove)
        # if random number is 1, go right
        elif move == 1:
            self.x0 = self.x0 + xmove
            self.canvas.move(self.car, xmove, ymove)
            self.canvas.move(self.text, xmove, ymove)
        elif move =="crash":
            self.canvas.move(self.car, 0, 0)
        # if random number is -1, go left
        else:
            self.canvas.move(self.car, -xmove, ymove)
            self.canvas.move(self.text, -xmove, ymove)
        self.canvas.update()
        #time.sleep(0.000002)
        #self.car_off_road(road1_arr)
        #return True

    def car_coords(self):
        """Returns the cars coordinates to test if it has it the wall of the road"""
        return self.canvas.coords(self.car)

    def crash(self, road, ROAD_DISTANCE):
        """TODO: This method does nothing so far"""
        for i in range(len(road)):
            print("x0: " + str(self.x0) + " road[i]: " + str(int(road[i])))
            print("car width: " + str(self.x0+self.car_width) + " other road: " + str(int(road[i]+ROAD_DISTANCE)))
            if (self.x0 <= int(road[i]) and self.y0 == int(road[i]+1)) or (self.x0+self.car_width >= int(road[i]+ROAD_DISTANCE) and self.y0 == int(road[i]+1)):
                print("crash")
                return True
            i = i+1
        return False

    def car_off_road(self, road1_arr):
        """This method should determine when the car either hits the side of the road
        or gets to the end of the road
        TODO: Finish the functionality of this method
        """
        car_pos = self.car_coords()
        car_pos_y = int(car_pos[1])
        road_pos = int(road1_arr[int(car_pos_y / self.car_length)])
        #print("car position " + str(car_pos_y))
        #print("road_pos " + str(road_pos))