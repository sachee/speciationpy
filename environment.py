# Sasha Solomon #
# 6/18/2012     #
# Speciation    # 

from __future__ import division
import numpy as np
import sys
from ecosystem import Ecosystem
SIGMA = .356 # to be put in main func later
MAX_CAP = 500 #to be in main func later # carrying capacity
num_env_fac = 3
grid_size = 3
loci = 3
dispersion_radius = 1


class Environment:
    def __init__(self, grid_size, loci, num_env_fac):
        self.grid = []
        self.grid_size = grid_size
        self.generate(loci, num_env_fac)
        
    def generate(self, loci, num_env_fac): # generate environment and populate with ecosystems #
        for i in range(0, grid_size): # x coords
            self.grid.append([]) # build the rows
            for j in range(0, grid_size): # y coords
                eco = Ecosystem(num_env_fac, SIGMA, MAX_CAP, (i, j)) # create an ecosystem at the plot
                eco.connect(grid_size) # connect the ecosystem to its neighbors
                self.grid[i].append(eco) # put ecosystem into environment grid
                if( i == 0 and j == 0): # this is the initial founder square with the initial 500 inds
                    eco.populate(MAX_CAP, loci, SIGMA)

    def disperse(self):
        dispersed_grid = self.grid # this will be the resulting grid after dispersal
        for env in self.grid:
            for eco in env:
                for ind in eco.population.members:
                    preferences = [] # up to 9 preferences for the 9 ecosystems surrounding the individual's current ecosystem
                    for coords in eco.neighbors:
                        ind.find_preference(self.grid[coords[0]][coords[1]].eco_type) # find the preference using the coordinates of the surrounding ecoystems
                        # calc pref for i, j
                        # do all the changes to percentages
                        # choose num between 0 and 1, if falls in bucket, choose that ecosystem to move to.

    def print_env(self):
        #print '-------' * grid_size
        for env in self.grid:
            for eco in env:
                #print '|' ,
               # for ind in eco.population.members:
                number_of_inds = str(len(eco.population.members))
                if len(number_of_inds) == 2:
                    print '| ' ,
                if len(number_of_inds) == 1:
                    print '|  ',
                else:
                    print '|',
                #print len(eco.population.members),
                print eco.neighbors,
               # print '|',
                   # sys.stdout.write("o")
                        
            #    sys.stdout.write( ' | ')
                #sys.stdout.write(eco.coordinates)
               # sys.stdout.write(eco.eco_type)
            if eco.coordinates[1] == self.grid_size - 1:
                sys.stdout.write(' | ')
                print
                print


def main():
    E = Environment(grid_size, loci, num_env_fac)
    E.print_env()
    E.disperse()
    E.print_env()

if __name__ == "__main__":
    main()
