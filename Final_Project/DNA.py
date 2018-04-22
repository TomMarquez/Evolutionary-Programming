"""DNA class
An array of binary numbers that will guide the car

One strain of DNA = [2]
    - 00 -> stop
    - 01 -> right
    - 10 -> left
    - 11 -> forward
"""

import random

class DNA(object):
    def __init__(self, dna_arr=[]):
        self.dna_arr = dna_arr
        self.arr_size = 100