# Sasha Solomon #
# 6/18/2012     #
# Speciation    #

from __future__ import division
import numpy as np
import random as rand

class ecosystem:
    def __init__(self, loci, env_fac, SIGMA, MAX_CAP, coords):
        self.capacity = MAX_CAP*SIGMA
        self.niche_type =  rand.randrange(0, 2**env_fac) # type of ecosystem 2**k niche types
        self.coordinates = coords # coordinates of ecosystem's location in nXn grid
        self.neighbors = [] # where the ecosystem is/who it is connected to in the nXn grid

    def connect(self): # connect the ecosystem to its neighbors #
        if i - 1 >= 0: # if neighbors exist to the left
            self.neighbors.append((i-1, j))
            if j - 1 >= 0: # if neighbors exist to the above left
                self.neighbors.append((i-1, j-1))
        if j - 1 >= 0: # if neighbors exist above
            self.neighbors.append((i, j-1))
            if i + 1 < grid_size: # if neighbors exist to the above right
                self.neighbors.append(i+1, j-1))
                    
        
