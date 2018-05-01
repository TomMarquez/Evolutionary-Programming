from Population import Population
from Window import Window
import tkinter as tk
from tkinter import *
import random
import time
import random

class Main:
	pop = Population(20, 70, 10)
	pop.init_pop()
	road = 40
	obstacle = 0
	obstacles = []
	for i in range(140):
		if random.randint(0, 10) == 0:
			obstacles.append(random.randint(0, 9))
		else:
			obstacles.append(-1)
	print(obstacles)
	while(not pop.done()):
		is_obstacle = random.randint(0, 10) == 0
		if is_obstacle:
			obstacle = random.randint(0, 9)
		road_move = random.randint(0,2) -1
		pop.make_move(road + road_move, obstacle, -1)
	pop.print_fit()
	pop.rank_fitness()
	pop.print_fit()
	pop.breed(20, 95)
	pop



	# root window
	root = Tk()
	root.geometry("800x800")
	# create instance
	app = Window(root)

	# main loop
	root.mainloop()