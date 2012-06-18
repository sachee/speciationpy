# Sasha Solomon #
# 6/18/2012     #
# Speciation    #

from __future__ import division
import numpy as np
SIGMA = .356 # to be put in main func later
MAX_CAP = 500 #to be in main func later
class environment:
    def __init__(self, grid_size, loci, env_fac):
        self.grid = []
        self.generate()
        
    def generate(self): # generate environment and populate with ecosystems #
        for i in range(0, grid_size + 1): # x coords
            self.grid.append([]) # build the rows
            for j in range(0, grid_size + 1): # y coords
                ecosystem(loci, env_fac, SIGMA, MAX_CAP, (i, j)) # create an ecosystem at the plot
                ecosystem.connect() # connect the ecosystem to its neighbors
        
        
