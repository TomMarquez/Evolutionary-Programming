'''
Window Class

This will provide the window for displaying the simulation

'''

import tkinter as tk
from tkinter import *
import random
import time

from Car import Car
from Road import Road
from Obstacle import Obstacle

OBSTACLE_SIZE = 5
ROAD1_START = 300
ROAD_DISTANCE = 100
CAR_START = ROAD1_START + ROAD_DISTANCE - 50
CAR_WIDTH = 10
CAR_LENGTH = 5
Y_SIZE = 700

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
        #canvas.create_rectangle(400, 600, 430, 660, outline="gray", fill="gray", width=2)

        #canvas.pack(fill=BOTH, expand=1)
        # d = [ [None for y in range(2) ] for x in range(2)]
        self.grid = []
        self.cars = []
        self.obstacle = []

        road = Road(canvas, ROAD1_START, 0, ROAD_DISTANCE, Y_SIZE)
        road1_array, road2_array = road.line_coords()
        road1_array = road.get_x1_coords()

        car = Car(canvas, CAR_START, 0, CAR_WIDTH, CAR_LENGTH)
        obstacle1 = Obstacle(canvas, OBSTACLE_SIZE, 150, 150, road1_array, ROAD_DISTANCE)
        obs_pos = obstacle1.obstacle_coords()
        for i in range(len(road1_array)):
            roadx = road1_array[i]
            self.grid.append(roadx)
    
        #obstacle1.get_x_y_coords(road1_array, road2_array)

        done = car.car_update(road1_array, road2_array, obs_pos, ROAD_DISTANCE)
        while done:
            done = car.car_update(road1_array, road2_array, obs_pos, ROAD_DISTANCE)
            if done == False:
                print("new road")
                new_road_start = road1_array[len(road1_array)-1]
                canvas.delete("all")
                #canvas.after(1000, canvas.delete, road)
                #canvas.delete(road)
                canvas.update()
                road = Road(canvas, new_road_start, 0, ROAD_DISTANCE, Y_SIZE)
                car = Car(canvas, CAR_START, 0, CAR_WIDTH, CAR_LENGTH)
                obstacle1 = Obstacle(canvas, OBSTACLE_SIZE, 150, 150, road1_array, ROAD_DISTANCE)
                road1_array, road2_array = road.line_coords()
                road1_array = road.get_x1_coords()
                obs_pos = obstacle1.obstacle_coords()
                done = car.car_update(road1_array, road2_array, obs_pos, ROAD_DISTANCE)

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