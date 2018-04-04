#################################################################################################################
##
##	Elisha Waugh
##	CSCE 412
##	Project 2
##
#################################################################################################################

### imports #####################################################################################################
import math 																									#
import random as rd 																							#
import numpy as np 																								#
#################################################################################################################

### Random seeds ################################################################################################
rd.seed(15)																									#
np.random.seed(100330)																							#
#################################################################################################################

### Changeable Global Variables #################################################################################
num_parents		= 3				# Number of parents.															#
num_offspring	= 21			# Number of offspring.															#
term_count		= 100			# Number of iterations the program will run. 									#
sig 			= [.08,.08]		# The step size of the mutation.												#
#################################################################################################################

### Other Global Variables ######################################################################################
parents 	= []				# A list of all the parents. [X one value, X two value, Fitness], [...], ...	#
offspring	= []				# A list of all the offspring. [X one value, X two value, Fitness], [...], ...	#
#################################################################################################################

def initialize_parents():
	global parents
	for i in range(num_parents):
		x_one = rd.uniform(-3.0, 12.0)
		x_two = rd.uniform(4.0, 6.0)
		fit = fitness(x_one, x_two)
		parents.append([x_one, x_two, fit])

def fitness(x_one, x_two):
	return 21.5 + x_one * math.sin(4 * math.pi * x_one) + x_two * math.sin(20 * math.pi * x_two)

def recombination():
	global offspring
	offspring = []
	for i in range(num_offspring):
		y_one = 0
		y_two = 0
		while not(y_one >= -3 and y_one <= 12 and y_two >= 4 and y_two <= 6):
			selected = rd.randint(0, num_parents-1)
			N =  [np.random.normal(0, 1), np.random.normal(0,1)]
			y_one = parents[selected][0] + sig[0] * N[0] 
			y_two = parents[selected][1] + sig[1] * N[1]
			fit = fitness(y_one, y_two)
		offspring.append([y_one, y_two, fit])

def new_parents():
	global parents
	top_fit = [] 
	fit_array = []
	# make fit array
	for i in range(num_offspring):
		fit_array.append(offspring[i][2])

	for i in range(num_parents):
		max = -99999999999
		max_index = 0
		for j in range(num_offspring):
			if fit_array[j] > max and not_in_arr(top_fit, j):
				max = fit_array[j]
				max_index = j
		top_fit.append([max, max_index])
	parents = []
	for i in range(num_parents):
		parents.append(offspring[top_fit[i][1]])
	print(top_fit)

def not_in_arr(arr, selected):
	for i in range(len(arr)):
		if arr[i][1] == selected:
			return False
	return True

################################ Main ########### Main ########## Main ##########################################
def main():
	initialize_parents()
	print()
	print(parents)
	print()
	# Main loop of program. it runs untill term_count is reached.
	for i in range(term_count):
		recombination()
		print(offspring)
		print()
		new_parents()
		print()
		print(parents)
		print()

if __name__ == "__main__":
    main()