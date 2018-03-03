#####################################################################
## Name: Tom Marquez and Elisha Waugh
##
## Assignment: Evolution Strategy Assignment
##
## Evolve a solution that maximizes the function:
##  f(x1, x2) = 21.5 + x1 * sin(4pix1) + x2 * sin(20pix2)
##
## constraints: -3.0 <= x1 <= 12.0 and 4.0 <= x2 <= 6.0
##
## Use discreet global recombination to create x values of each
## offspring, and intermediary global recombination to create the 
## sigma values. 
##
## Recombination will occur lambda times, producing lambda offspring
##
## Use uncorrelated mutations with n step sizes to modify each of the 
## offspring produced via recombination.
##
## Begin program with the following parameters:
##  mu = 3                      (number of parents)
##  lambda = 21                 (number of offspring)
##  (mu, lambda)selection       (the best mu offspring replace the parents)
##  sigma initial = 1           (initial value of the mutation step size in each dimension)
##  termination count = 10,000  (stop after 10,000 fitness evauations)
##  tau = 1/sqrt(2*n)           (the overall learning rate)
##  tau = 1/sqrt(2*sqrt(n))     (the coordinate-specific learning rate
####################################################################
from random import *

### Changeable Global Variables #################################################################################
mu = 3                          # number of parents
lam = 21                        # number of offspring
sigma = 1                       # initial value of mutation step size
termination = 10000             # terminate program

#################################################################################################################


