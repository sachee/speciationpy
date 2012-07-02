# Sasha Solomon #
# 6/18/2012     #
# Speciation    #

from __future__ import division
import numpy as np
import random as rand
from population import Population

class Ecosystem:
    def __init__(self, num_env_fac, SIGMA, MAX_CAP, coords):
        self.capacity = MAX_CAP*SIGMA
        self.num_env_fac = num_env_fac # number of environmental factors that determines niche types
        self.eco_type =  self.generate_eco(self.num_env_fac) # type of ecosystem 2**k possible niche types, k long
        self.coordinates = coords # coordinates of ecosystem's location in nXn grid
        self.neighbors = [] # where the ecosystem is/who it is connected to in the nXn grid
        self.population = Population()

    def connect(self, edge): # connect the ecosystem to its neighbors #
        i = self.coordinates[0] # i coordinate of position in grid (like matrix coords)
        j = self.coordinates[1] # j coordinate of position in grid (like matrix coords)
        if i - 1 >= 0: # if neighbors exist to the left
            self.neighbors.append((i-1, j))
            if j - 1 >= 0: # if neighbors exist to the above left
                self.neighbors.append((i-1, j-1))
        if j - 1 >= 0: # if neighbors exist above
            self.neighbors.append((i, j-1))
            if i + 1 < edge: # if neighbors exist to the above right
                self.neighbors.append((i+1, j-1))
                    
        
    def generate_eco(self, k): # generate an ecosystem with k environmental factors
        eco = []
        for _ in range(k): # randomly choose a niche and whether it is "on" or "off"
            eco.append(bool(rand.getrandbits(1)))
        return eco

    def populate(self, carry_cap, loci, SIGMA):
        self.population.initial_pop(carry_cap, loci, self.num_env_fac, self.eco_type, SIGMA)
        
