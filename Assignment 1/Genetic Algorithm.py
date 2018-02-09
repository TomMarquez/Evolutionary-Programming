###################################################
## Name: Tom Marquez and Elisha Waugh
##
## Assignment: LCS Genetic Algorithm
##
##
##
##
###################################################
from random import *

#   Global Variables
population_size = 10
k = 0
smallest_string = ""
largest_string = ""
pop = [] 

#   The population(pop[]) is a list of samples(test objects); 
#   each sample starts with an array (size k) of zeros and ones, 
#   next it has a string that is created by takeing the smallest string and keeping the leters that correspond to a one in the array,
#   last, it has it fitness value at the end of the list.

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

def mating_pool():
    total_fitness = 0
    roulette_wheel = []
    for i in range(0, population_size):
        total_fitness =+ pop[i][k+1]
    
    return x

def main():
    global k
    global smallest_string
    global largest_string
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
    print(pop)

if __name__ == "__main__":
    main()
