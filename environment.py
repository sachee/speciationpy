# Sasha Solomon #
# 6/18/2012     #
# Speciation    # 

from __future__ import division
import numpy as np
import sys
import math
from ecosystem import Ecosystem
import random as rand
from copy import deepcopy
from parameters import Parameters




class Environment:
    def __init__(self, P):
        self.grid = []
        self.grid_size = P.grid_size # a grid_sizeXgrid_size grid, i.e. nXn grid
        self.generate(P)
        
    def generate(self, P): # generate environment and populate with ecosystems #
        for i in range(0, P.grid_size): # x coords
            self.grid.append([]) # build the rows
            for j in range(0, P.grid_size): # y coords
                eco = Ecosystem(P, (i, j)) # create an ecosystem at the plot
                eco.connect(P.grid_size) # connect the ecosystem to its neighbors
                self.grid[i].append(eco) # put ecosystem into environment grid
                if( i == 0 and j == 0): # this is the initial founder square with the initial 500 inds
                    eco.populate(P)

    def disperse(self):
        dispersed_grid = deepcopy(self.grid) # this will be the resulting grid after dispersal
        dispersed_grid = self.clean_env(dispersed_grid) # clean each pop to make way for dispersal
        for env in self.grid:
            for eco in env:
                for ind in eco.population.members:
                    preferences = self.find_prefs(eco, ind) # up to 9 preferences for the 9 ecosystems surrounding the individual's current ecosystem
                    
                    pref_probs = self.convert_prefs(preferences) # converts prefs to probabilities
                    choosen_env = self.choose_env(pref_probs) # chooses environment to move to based on probabilities
                    
                    x, y = preferences[choosen_env][0] # get coordinates of chosen env
                    dispersed_grid[x][y].population.members.append(ind) # add ind to that ecosytem's population
                    
        self.grid = dispersed_grid

    def mate(self, P):
        for env in self.grid:
            for eco in env:
                    eco.population.selection(P.MAX_CAP) # perform selection
                    eco.population.mate(P) # the remaining individuals get to mate

    def find_prefs(self, eco, ind): # find the preferences for a specific ecosystem of an individual
        preferences = []
        for coords in eco.neighbors:
            pref = ind.find_preference(self.grid[coords[0]][coords[1]].eco_type) # find the preference using the coordinates of the surrounding ecoystems
            preferences.append((coords, pref))

        pref = ind.find_preference(eco.eco_type) # find ind's preference for its current home
        preferences.insert(4, (eco.coordinates, pref)) # add that eco's coordinates and preference into the correct position in the preference list
        return preferences

    def convert_prefs(self, preferences):
        total_pref = 0
        pref_probs = [] # list of individual's preferences as probabilities
        for i in range(len(preferences)):
            coords, pref = preferences[i]
            total_pref += pref

        for i in range(len(preferences)):
            coords, pref = preferences[i]
            pref_prob = pref/total_pref # the individual's preference as a probability
            pref_probs.append(pref_prob)
        return pref_probs


    def choose_env(self, probs): # choose an ecoystem square to move to based on individual's preference probs
        rand_num = rand.random() # pick random num between 0 and 1
        result = probs[0] - rand_num # initialize result. Result will determine what eco is chosen (proportional)
        i = 0
        while result > 0:   
            i+=1
            if i == len(probs):
                i = 0 # loop back around if still not <= 0
            result -= probs[i] # proportional probability   
        return i # return the index of where the ecosystem is located

    def clean_env(self, grid): # 'cleans' the environment by removing ALL individuals
        for env in grid:
            for eco in env:
                eco.population.members = []
        return grid
                
    def eco_extinction(self, extinction_rate, num_env_fac):
        total_ecosystems = self.grid_size*self.grid_size
        num_extinct = self.find_num_extinct(extinction_rate, total_ecosystems) # find the number of ecosystems that will go extinct
        if num_extinct > 0:
            chosen = set() # a set of the chosen ecosystems to go extinct
            while len(chosen) != num_extinct: # get distinct ecos
                chosen.add(rand.randrange(total_ecosystems))
            eco_num = 0 # used to determine the 'number' of the ecosystem
            for env in self.grid:
                for eco in env:
                    if eco_num in chosen: # if the eco number matches a number in chosen, exterminate!
                        eco.exterminate()
                    eco_num += 1


        
    # ''' finds the number of ecosystems to go extinct ''' #            
    def find_num_extinct(self, expected_value, N):
        L = math.e**((-1)*expected_value)
        k = 1
        p = 1
        p*= rand.random() # initial p
        while p > L:
            k+=1
            p*= rand.random()
        return (k - 1)*N


    def print_env(self):
        #print '-------' * grid_size
        for env in self.grid:
            for eco in env:
                #print '|' ,
                #for ind in eco.population.members:
                number_of_inds = str(len(eco.population.members))
                if len(number_of_inds) == 2:
                    print '| ' ,
                elif len(number_of_inds) == 1:
                    print '|  ',
                else:
                    print '|',
                print len(eco.population.members),
                #print eco.neighbors,
               # print '|',
                   # sys.stdout.write("o")
                        
            #    sys.stdout.write( ' | ')
                #sys.stdout.write(eco.coordinates)
               # sys.stdout.write(eco.eco_type)
            if eco.coordinates[1] == self.grid_size - 1:
                sys.stdout.write(' | ')
                print
                print
        print


def main():
    P = Parameters() # create parameter set
    E = Environment(P)
    E.print_env()
    generations = 10
    for generation in range(generations):
        E.disperse() # individuals disperse to neighboring ecosystems
        E.mate(P) # individuals mate
        E.eco_extinction(P.extinction_rate, P.num_env_fac) #ecosystems and inviduals go have a probability of going extinct
        E.print_env()

if __name__ == "__main__":
    main()
