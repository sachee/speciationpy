from __future__ import division
import numpy as np
import random as rand

class Individual:
    def __init__(self, loci, num_env_fac, eco_type, SIGMA):
        self.loci = loci
        self.sigma = SIGMA # strength of selection for local adaptation
        self.ecosystem = eco_type # the ecosystem the ind is currently living in
        self.genome = self.generate_genome(num_env_fac)
        self.fitness = self.find_fitness()

    def generate_genome(self, k): # generate an ecosystem with k environmental factors
        trait_bit = True # all inds start with traits at 1/2 (homozygotes)
        genome = []
        for i in range(k): # randomly choose a niche and whether it is "on" or "off"
            genome.append([])
            for _ in range(self.loci):
                genome[i].append(trait_bit)
                trait_bit = not trait_bit
            trait_bit = True
               # genome[i].append(bool(rand.getrandbits(1))) #each trait has a x loci, and each genome is k traits long
        return genome
    
    def find_fitness(self):
        w = [] # fitness component matrix
        overall_fitness = 1
        theta = self.ecosystem
        x = self.genome[0] #first trait controls ecology
        for i in range(self.loci):
            w.append(np.exp( ( ( -(x[i] - theta[i]) )**2 )/(2*self.sigma**2) ) )
            overall_fitness *= w[i]
        return overall_fitness

    def find_preference(self):
        p = [] # preference component matrix
        overall_pref = 1
        theta = self.ecosystem
        y = self.genome[1] # second trait controls preference
        for i in range(self.loci):
            if theta[i] == 1:
                p.append(.5+1*(y[i] - .5)) # where a[i] = 1 i.e. possible strength is 1
        
        
            
        
