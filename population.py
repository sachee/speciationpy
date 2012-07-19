# Sasha Solomon #
# 6/18/2012     #
# Speciation    #

from __future__ import division
import numpy as np
from individual import Individual
import random as rand

class Population:
    def __init__(self):
        self.members = []
        self.size = 0
        #self.carry_cap = 0
        self.b = 4 # average number of offspring per female
        self.num_juveniles = self.find_num_juveniles()

    def initial_pop(self, P, eco_type): # initial pop of adults
        for _ in range(P.MAX_CAP):
            ind = Individual(P, eco_type)
            ind.juvenile = False
            self.members.append(ind)
            self.size+=1
        #self.carry_cap = carry_cap

    # ''' select individuals that will survive to the age of reproduction ''' #
    def selection(self, MAX_CAP):
        N = self.find_num_juveniles()
        for ind in self.members:
            K = ind.fitness*MAX_CAP # as defined in the paper
            v = 1/(1 + (self.b - 1) * (N/K))
            if not self.select_ind(v): # if the individual was not selected to live
                self.members.remove(ind) # remove that ind from the population

    # ''' using proportional probability, determine if ind lives '''#
    def select_ind(self, prob):
        rand_num = rand.random() # pick random num between 0 and 1
        probs = (prob, 1-prob) # need both the actual probability AND the probability that the ind WON'T live
        result = prob - rand_num # initialize result. Result will determine what eco is chosen (proportional)
        i = 0
        while result > 0:   
            result -= probs[i] # proportional probability   
        return bool(i) # return the index of where the ecosystem is located

    def find_num_juveniles(self):
        total = 0
        for ind in self.members:
            if ind.juvenile: # if individual is a juvenile
                total+=1


    def poisson_dist(N):
        L = math.e**(-1)*N
        k = 1
        p = 1
        p*= rand.random() # initial p
        while p > L:
            k+=1
            p*= rand.random()
        return k - 1
         



    def mate(self):
        for female in self.members: # each ind in the pop is a female once
            male = rand.choice(self.members)
            while male == female: # make sure the inds are mating with themselves!
                male = rand.choice(self.members)
                num_offspring = poisson_dist(self.b) # find number of offspring based on avg offspring
                for _ in range(num_offspring):
                    self.mutation()
                    self.crossover()
            #mutation
            #crossover

    def create_offspring(self):
        pass

    def mutation(self):
        pass

    def crossover(self):
        pass