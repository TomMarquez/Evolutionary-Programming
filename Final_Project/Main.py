from Population import Population
from Window import Window
import tkinter as tk
from tkinter import *
import random
import time
import random
import matplotlib.pyplot as plt



def main():
	pop_size = 100
	iteration = 10000
	max_fit = 0
	top_fit = 0
	average_fit = 0
	pop = Population(pop_size, 10, 10)
	pop.init_pop()
	road = 1
	iterations = []
	top_fits = []
	max_fits = []

	for i in range(iteration):
		iterations.append(i)
		
		obstacle = -1
		while(not pop.done()):
			if random.randint(0, 10) == 0:
				obstacle = random.randint(0, 9)
			road_move = random.randint(0,2) -1
			pop.make_move(road, obstacle, road_move)
			#road = road + road_move
		pop.rank_fitness()
		fit_sum = 0
		top_fit = pop.fit[0][1]
		if max_fit < top_fit:
			max_fit = top_fit
		for j in range(pop_size):
			fit_sum += pop.fit[j][1]
		average_fit = fit_sum / pop_size
		top_fits.append(top_fit)
		max_fits.append(max_fit)
		pop.breed(pop_size, 95, 2)
		print("Iteration: " + str(i))
		print("Max Fitness: " + str(max_fit))
		print("Top Fitness: " + str(top_fit))
		print("Average Fitness: " + str(average_fit))

	plt.plot(top_fits, label= 'Top Fit')
	plt.plot(max_fits, label = 'Max Fit')
	plt.title("Fitness vs Time(Population: 100)")
	plt.ylabel('Fitness')
	plt.xlabel('Iterations')
	plt.legend();
	plt.show()

if __name__=='__main__':
    main()
