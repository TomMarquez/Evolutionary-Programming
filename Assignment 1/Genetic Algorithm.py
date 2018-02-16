###################################################
## Name: Tom Marquez and Elisha Waugh
##
## Email: tmarquez@alaska.edu, 
## Assignment: LCS Genetic Algorithm
##
##
##
##
###################################################
from random import *

#   Global Variables
population_size = 10
k =  0 # size of smallest string
smallest_string = ""
largest_string = ""
pop = [] 

#   The population(pop[]) is a list of samples(test objects); 
#   each sample starts with an array (size k) of zeros and ones, 
#   next it has a string that is created by takeing the smallest string and keeping the leters that correspond to a one in the array,
#   last, it has it fitness value at the end of the list.

# initialize_pop
# Creates a population of size population_size
# where each member is k length (the length of the smallest string)
def initialize_pop():
    for i in range(0, population_size):
        pop.append([])
        for j in range (0, k):
            pop[i].append(randint(0, 1))
        pop[i].append("")
        pop[i].append(0)

def get_substrings():
    for i in range(0, population_size):
        for j in range(0, k):
            if pop[i][j] == 1:
                pop[i][k] = pop[i][k] + smallest_string[j]

def fitness(sample, i, j, fit_score):
    sub_string = str(sample[k])
    if i >= len(sub_string):
        return 0
    elif j >= len(largest_string):
        return fitness(sample, i+1, 0, fit_score)
    elif sub_string[i] == largest_string[j]:
        return 1 + fitness(sample, i+1, j+1, fit_score+1)
    else:
        return fitness(sample, i, j + 1, fit_score)

# mating_pool
# 
def mating_pool(new_pop_size):
    total_fitness = []
    roulette_wheel = []
    result = []
    for i in range(0, population_size):
        total_fitness.append(pop[i][k+1])
    for i in range(0, population_size):
        for j in range(0, total_fitness[i]):
            roulette_wheel.append(pop[i])
    for i in range(0, new_pop_size):
        result.append(roulette_wheel[randint(0, len(roulette_wheel)-1)])
    return result

# breed
# Takes in the mating pool and finds a pair
# to breed. Each member has a 95% chance of 
# breeding. Once a pair is found, 1-point crossover
# is performed. If there is one member left in the 
# mate_match array, it is appended to the result. 
def breed(mating_pool):
    mate_match = []
    result = []
    for i in range(0, len(mating_pool)):
        if randint(0, 100) >= 6:
           mate_match.append(mating_pool[i])
        else:
            result.append(mating_pool[i])
        if len(mate_match) == 2:
            x, y = cross_over(mate_match)
            result.append(x)
            result.append(y)
            mate_match = []
    if len(mate_match) == 1:
        result.append(mate_match[0])
    return result

# cross_over
# 1-point crossover is preformed on a pair
def cross_over(mate_match):
    cross_point = randint(0, k-1)
    temp = 0
    for i in range(0, cross_point):
        temp = mate_match[0][i]
        mate_match[0][i] = mate_match[1][i]
        mate_match[1][i] = temp
    x = mate_match[0]
    y = mate_match[1]
    return x, y;

# mutation
# Mutation is preformed on the population.
# Each member has a 1/population size chance
# of being mutated, and each gene of the selected 
# member has a 1/k chance of mutating.
def mutation():
    global pop
    for i in range(0, len(pop)):
        if randint(0, len(pop)-1) == 0:
            for j in range(0, k):
                if randint(0, k-1) == 0:
                    if pop[i][j] == 0:
                        pop[i][j] = 1
                    else:
                        pop[i][j] = 0
                    


def main():
    max_fit = []
    gen = 0
    max_fit_last_beat = 0
    global k, pop, smallest_string, largest_string
    string_one = input("enter string one \n")
    string_two = input("enter string two \n")
    #Determin which string is smaller and make k the length of the smaller string
    if len(string_one) > len(string_two):
        k = len(string_two)
        smallest_string = string_two
        largest_string = string_one
    else:
        k = len(string_one)
        smallest_string = string_one
        largest_string = string_two
    initialize_pop()
    get_substrings()
    for i in range(0, population_size):
        pop[i][k+1] = fitness(pop[i], 0, 0, 0)
    max_fit = pop[i]

    while max_fit_last_beat < 10:
        for i in range(0, population_size):
            pop[i][k+1] = fitness(pop[i], 0, 0, 0)
        print("population :\n" + str(pop))
        print("\n") 
        print("gen: " + str(gen) + " max_fit_last_beat : " + str(max_fit_last_beat) + "\n")
        for i in range(0, population_size):
            if max_fit[k+1] < pop[i][k+1]:
                max_fit = pop[i]
        new_pop = mating_pool(population_size)
        pop = breed(new_pop)
        gen += 1

        max_fit_last_beat +=1
    print("done : "  + str(max_fit))


if __name__ == "__main__":
    main()
