# Sasha Solomon #
# 6/18/2012     #
# Speciation    #

from __future__ import division
import numpy as np
import random as rand
from population import Population

class Ecosystem:
    def __init__(self, P, coords):
        self.capacity = P.MAX_CAP*P.SIGMA
        # number of environmental factors that determines niche types
        self.eco_type =  self.generate_eco(P.num_env_fac) # type of ecosystem 2**k possible niche types, k long
        self.coordinates = coords # coordinates of ecosystem's location in nXn grid
        self.neighbors = [] # where the ecosystem is/who it is connected to in the nXn grid
        self.population = Population(P.b)

    def connect(self, edge): # connect the ecosystem to its neighbors #
        i = self.coordinates[0] # i coordinate of position in grid (like matrix coords)
        j = self.coordinates[1] # j coordinate of position in grid (like matrix coords)
        # this system assures neighbors are sorted according to their coordinates
        if i - 1 >= 0: # if neighbors exist to the left
            if j - 1 >= 0: # if neighbors exist to the above left
                self.neighbors.append((i-1, j-1))
            self.neighbors.append((i-1, j))
            if j + 1 < edge:
                self.neighbors.append((i-1, j+1))
        if j - 1 >= 0: # if neighbors exist above
            self.neighbors.append((i, j-1))
        if j + 1 < edge:
            self.neighbors.append((i, j+1))
        if i + 1 < edge:  
            if j - 1 >= 0:
                self.neighbors.append((i+1, j-1)) # if neighbors exist to the above right
            self.neighbors.append((i+1, j))
            if j + 1 < edge:
                self.neighbors.append((i+1, j+1)) 
        
    def generate_eco(self, k): # generate an ecosystem with k environmental factors
        eco = []
        for _ in range(k): # randomly choose a niche and whether it is "on" or "off"
            eco.append(bool(rand.getrandbits(1)))
        return eco

    def populate(self, P):
        self.population.initial_pop(P, self.eco_type)

    def exterminate(): # 'cleans' the ecosystem and removes all individuals
        pass

