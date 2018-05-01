'''
Window Class

This will provide the window for displaying the simulation

'''

from Population import Population
import tkinter as tk
from tkinter import *
import random
import time
import random

from Car import Car
from Road import Road
from Obstacle import Obstacle


pop = Population(10, 80, 10)
# Class for creating the window
class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        OBSTACLE_SIZE = 5
        ROAD1_START = 300
        ROAD_DISTANCE = 100
        CAR_WIDTH = 10
        CAR_START = ROAD1_START + ROAD_DISTANCE - 50
        CAR_LENGTH = 5
        Y_SIZE = 700

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
        self.obstacles = []

        road = Road(canvas, ROAD1_START, 0, ROAD_DISTANCE, Y_SIZE)
        road1_array, road2_array = road.line_coords()
        road1_array = road.get_x1_coords()
        x = ROAD1_START
        for i in range(10):
            car = Car(canvas, x, 0, CAR_WIDTH, CAR_LENGTH, str(i))
            self.cars.append(car)
            x += 10
        #obs_pos = obstacle1.obstacle_coords()
        for i in range(len(road1_array)):
            roadx = road1_array[i]
            self.grid.append(roadx)
        for i in range(70):
            if random.randint(0, 10) == 0:
                self.obstacles.append(random.randint(0, 9))
            else:
                self.obstacles.append(-1)

        for i in range(70):
            if self.obstacles[i] != -1:
                Obstacle(canvas, OBSTACLE_SIZE, i*10, self.grid[i]+self.obstacles[i]*10, road1_array, ROAD_DISTANCE)
        #obstacle1.get_x_y_coords(road1_array, road2_array)

        # done = car.car_update(road1_array, road2_array, obs_pos, ROAD_DISTANCE)

        y = 0
        crashed = [False] * 10
        while not pop.done():
            j = 0
            
            for j in range(len(self.cars)):
                if not pop.crashed[j]:
                    if j == 5:
                        print("Car " + str(j) + " position: " + str(self.cars[j].x0))
                        print("position: " + str(pop.car[j]))
                        print("obs: " + str(self.obstacles[y]))
                    move = pop.get_car(j).get_move(int(self.grid[y] / 10), pop.car[j], self.obstacles[y])
                    self.cars[j].car_update(road1_array, road2_array, ROAD_DISTANCE, move)
            if y == 0:
                pop.make_move(int(self.grid[y]/10), self.obstacles[y], 0)
                print(self.grid[y])
            else:
                pop.make_move(int(self.grid[y]/10), self.obstacles[y], int(( self.grid[y-1] - self.grid[y]) / 10))
                print(self.grid[y])
                if y == 69 :
                    print("new road")

                    new_road_start = road1_array[len(road1_array)-1]
                    new_x_coords = []
                    for i in range(len(self.cars)):
                        new_x_coords.append(self.cars[i].x0)
                    canvas.delete("all")
                    #canvas.after(1000, canvas.delete, road)
                    #canvas.delete(road)
                    canvas.update()
                    # redraw road
                    road = Road(canvas, new_road_start, 0, ROAD_DISTANCE, Y_SIZE)

                    self.cars = []
                    # redraw cars
                    for i in range(len(new_x_coords)):
                        car = Car(canvas, new_x_coords[i], 0, CAR_WIDTH, CAR_LENGTH, str(i))
                        self.cars.append(car)

                    road1_array, road2_array = road.line_coords()
                    road1_array = road.get_x1_coords()
                    #obs_pos = obstacle1.obstacle_coords()

                    self.grid = []
                    self.obstacles = []

                    for i in range(len(road1_array)):
                        roadx = road1_array[i]
                        self.grid.append(roadx)
                    for i in range(140):
                        if random.randint(0, 10) == 0:
                            self.obstacles.append(random.randint(0, 9))
                        else:
                            self.obstacles.append(-1)
                    for i in range(70):
                        if self.obstacles[i] != -1:
                            Obstacle(canvas, OBSTACLE_SIZE, i*10, self.grid[i]+self.obstacles[i]*10, road1_array, ROAD_DISTANCE)
                    #self.cars[j].car_update(road1_array, road2_array, ROAD_DISTANCE, move)
                    print("new car array size: " + str(len(self.cars)))
                    y = 2
            
            y += 1
        print(pop.fit)

    def pop_make_move():
        while(not pop.done()):
            road_move = random.randint(0,2) -1
            pop.make_move(road + road_move, obstacle, -1)
        pop.print_fit()
        pop.rank_fitness()
        pop.print_fit()
        pop.breed(20, 95)

    def client_exit(self):
        exit()



#     # root window
#     root = Tk()
#     root.geometry("800x800")
#     # create instance
#     app = Window(root)

#     # main loop
#     root.mainloop()

def main():

    pop.init_pop()


    obstacle = 0
    

    root = Tk()
    root.geometry("800x800")
    # create instance
    app = Window(root)

    # main loop
    root.mainloop()



    # root window
    

if __name__=='__main__':
    main()