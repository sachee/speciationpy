from __future__ import division
import numpy as np
import random as rand
from trait import Trait

class Individual:
    def __init__(self, num_loci, num_env_fac, eco_type, SIGMA):
        self.num_loci = num_loci
        self.sigma = SIGMA # strength of selection for local adaptation
        self.ecosystem = eco_type # the ecosystem the ind is currently living in
        self.k = num_env_fac
        self.genome = self.generate_genome()
        self.fitness = self.find_fitness()
        self.juvenile = True # flag for if individual is juvenile. All inds begin as juveniles
        

    def generate_genome(self): # generate an ecosystem with k environmental factors
        ecological_chars = []
        preference_chars = []

        for i in range(self.k): # randomly choose a niche and whether it is "on" or "off"
            ecological_chars.append([]) # the 2k characteristics; ecological and preference
            preference_chars.append([])
            ecological_chars[i] = Trait(self.num_loci)
            preference_chars[i] = Trait(self.num_loci)

               # genome[i].append(bool(rand.getrandbits(1))) #each trait has a x loci, and each genome is k traits long
        return (ecological_chars, preference_chars) # the entire genome

    def convert(self, trait): # converts genome to format that can interact with ecosystem features
        total_on = 0 # counter for number of bits turned on i.e. number of 1's in the trait
        for i in range(self.num_loci):
            if trait.loci[i]:
                total_on += 1
        return total_on/self.num_loci

    
    def find_fitness(self):
        w = [] # fitness component matrix
        overall_fitness = 1
        theta = self.ecosystem
        x = self.genome[0] #first trait controls ecology
        for i in range(self.k):
            w.append(np.exp( ( ( -(self.convert(x[i]) - theta[i]) )**2 )/(2*self.sigma**2) ) )
            overall_fitness *= w[i]
        return overall_fitness

    def find_preference(self, ecosystem_niche):
        p = [] # preference component matrix
        overall_pref = 1
        theta = ecosystem_niche # the set of environmental factors that together create an ecological niche
        y = self.genome[1] # second trait controls preference
        for i in range(self.k):
            if theta[i] == 1:
                p.append(.5 + 1*(self.convert(y[i]) - .5)) # where a[i] = 1 i.e. possible strength is 1, + when theta == 1
            else: # theta == 0
                p.append(.5 - 1*(self.convert(y[i]) - .5)) # where a[i] = 1 i.e. possible strength is 1, - when theta == 0
            overall_pref *= p[i]
        return overall_pref
        
        
            
        
