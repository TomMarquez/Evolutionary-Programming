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

### Changeable Global Variables #################################################################################
population_size = 4            # Size of population                                                            #
number_of_iterations = 100      # number of times the programe will run after last time a new max was found     #
chance_of_breed = 95            # number between 0-100 that represents the percetage of chance of breading      #
mutation_on = True              # If set to true it will allow for mutations to happen                          #
#################################################################################################################

### Other Global Variables ######################################################################################
k =  0                          # Size of smallest string                                                       #
smallest_string = ""            # Smallest string                                                               #
largest_string = ""             #Largest string                                                                 #
#################################################################################################################

### Population ##################################################################################################
pop = []                                                                                                        #
#   The population(pop[]) is a list of samples(test objects)                                                    #
#   index: 0 to k-1             each sample starts with an array (size k) of zeros and ones,                    #
#   index: k                    next, it has a string that is created by takeing the smallest string and        #
#                                   keeping the leters that correspond to a one in the array,                   #
#   index: k+1                  next, it has it fitness value at the end of the list.                           #
#   index: k+2                  last, it has the longest valid substring (possible result)                      #
#################################################################################################################

### Test Strings ################################################################################################
test_string_one_A = "president"                                                                         
test_string_one_B = "providence"                                                                         
test_string_two_A = "fjglkjdfslgkjdfkgjthisaslkjflkasdjflka"                                                                         
test_string_two_B = "fjgthis" 
test_string_three_A = "ajlfkjadslkfjadslkjfadslkjftjoirgalksdnjdnrgorhoagnfdjgnerougdogodfgoirhgoiravodfngondfagndafgndfgndfngdfngfdngfdsng;ldfsngldfsng;ldfng;lndfslkgdflkgjdkjflkdjglkdfjg"
test_string_three_B = "lkajglksjtesnrknerjeoisjtoisejlesnnesjfanshfsdhgsngjkrngjnsjafnsdjkfnasjdng;snflkasdnjagdjlkdjglkjds"
test_string_four_A = "wordandthisstuffdogcathumanboardwallcomputer"
test_string_four_B = "thisstuffwall"
test_string_five_A = "adsfjiaoewjrioewnoirnewnruiewbriuewhiruhewuafbkjbgrbgiubrsdiugndiufhgiouergondsfjgnkjfbgjrbagjbnjgbdsiugbduhgoudfhgsoirndgoneroiugneruognerugbupaoihgoidfhngoidsnrognersoignerubgiueriuigbsrijgbdfijbgjdfbgjdfsgjdfpjsgnfdpojsgndopfisngerungiusperngiuprnsgundfuignfdiusghudsifhgiodfngiudfngsiusrndpiugsndfpiognfduiopsgnpiero"
test_string_five_B = "fksdajfoiewjoarrnwejrneriuiurhgiudfgjeriuberiuafbeiubfweiubfiuaebfiueabfiuebfiueabfiuasbiupgdpognerognerspjgnpdisfngpiodfsngpoifdsngpoisdfngopidfsngopidfipog"
#################################################################################################################

# initializes the population 
def initialize_pop():
    for i in range(0, population_size):
        pop.append([])
        for j in range (0, k):
            pop[i].append(randint(0, 1))
        pop[i].append("")   #substring of 1s and 0s
        pop[i].append(0)    #fitness
        pop[i].append("")   #longest possible valid substiring 

# gets the substring based on the ones and zeros from the smallest string
def get_substrings():
    for i in range(0, population_size):
        for j in range(0, k):
            if pop[i][j] == 1:
                pop[i][k] = pop[i][k] + smallest_string[j]

# fitness is calculated by looping throgh all objects in the population. The fitness score is the highest number of matching elements in the substring and the longest string
def fitness():
    global pop
    for i in range(0, population_size):     #loop through all population
        max_score = 0
        result = ""
        for j in range(0, len(pop[i][k])):  #go through all letters in substring
            score = 0
            str = ""
            m = j
            for l in range(0, len(largest_string)):           
                if pop[i][k][m] == largest_string[l]:
                    score += 1
                    str = str + largest_string[l]
                    if m < len(pop[i][k]) - 1:
                        m += 1
            if score > max_score:
                max_score = score
                result = str
        pop[i][k+1] = max_score
        pop[i][k+2] = result

# Thia function selects the mating pool at random based on fitness score. It uses a roulette wheel which is sized to the total fitness of all population.
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
    
# This function breads the given mating pool
def breed(mating_pool):
    mate_match = []
    result = []
    for i in range(0, len(mating_pool)):
        if randint(0, 100) >= 100 - chance_of_breed:
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

# This is a helper function for breed. it uses a random cross over point to mate two objects.
def cross_over(mate_match):
    cross_point = randint(0, k-1)
    temp = 0
    for i in range(0, cross_point):
        temp = mate_match[0][i]
        mate_match[0][i] = mate_match[1][i]
        mate_match[1][i] = temp
    x = mate_match[0]
    y = mate_match[1]
    return (x, y)

# If turned on in randomly selects bits to be fliped. An 1/population size chance of being selected. If selected each bit has 1/k chance of being fliped
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

################################ Main ########### Main ########## Main ##########################################
def main():
    max_fit = []
    gen = 1
    max_fit_last_beat = 0 # variable for which generation the highest value was found
    max_fit_value = 0 # variable for the highest fit value
    global k, pop, smallest_string, largest_string
    ##string_one = input("enter string one \n")
    ##string_two = input("enter string two \n")
    string_one = test_string_three_A
    string_two = test_string_three_B
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
    fitness()
    max_fit = pop[0]
    max_fit_last_beat = 1
    max_fit_value = pop[0][k+1]
    # Main loop of program. it runs untill it has not found a higher fitness in a set number of iterations.
    while gen < number_of_iterations and max_fit_value < k:
        fitness()
        for i in range(0, population_size):
            if max_fit[k+1] < pop[i][k+1]:
                max_fit = pop[i]
                max_fit_last_beat = gen #+= 1
                max_fit_value = pop[i][k+1]
        new_pop = mating_pool(population_size)
        pop = breed(new_pop)
        if mutation_on:
            mutation()
        gen += 1
        #print("population :\n" + str(pop))
        print("\n") 
        print("gen: " + str(gen) + " max_fit_last_beat : " + str(max_fit_last_beat) + "\n")
        print("Current max string: " + str(max_fit))

        #max_fit_last_beat +=1
    print("\n")
    print("done : the LCS is : "  + str(max_fit))
    print("\n")
    print("the generation is was found was : " + str(max_fit_last_beat) + " and the fit score is " + str(max_fit_value))


if __name__ == "__main__":
    main()
