from __future__ import division
import numpy as np
import random as rand
from genome import Genome
from trait import Trait

class Individual:
    def __init__(self, P, eco_type):
        self.num_loci = P.num_loci
        self.sigma = P.SIGMA # strength of selection for local adaptation
        self.eco_type = eco_type # the ecosystem the ind is currently living in
        self.k = P.num_env_fac
        self.genome = Genome(self.k, P.num_loci)
        self.fitness = self.find_fitness(self.eco_type)
        self.juvenile = True # flag for if individual is juvenile. All inds begin as juveniles
        

  #  def generate_genome(self): # generate an ecosystem with k environmental factors
#        ecological_chars = []
#        preference_chars = []

#        for i in range(self.k): # randomly choose a niche and whether it is "on" or "off"
#            ecological_chars.append([]) # the 2k characteristics; ecological and preference
#            preference_chars.append([])
#            ecological_chars[i] = Trait(self.num_loci)
#            preference_chars[i] = Trait(self.num_loci)

               # genome[i].append(bool(rand.getrandbits(1))) #each trait has a x loci, and each genome is k traits long
#        return (ecological_chars, preference_chars) # the entire genome

    def genome_size(self):
        return self.genome.length*self.k*self.num_loci

    def convert(self, trait): # converts genome to format that can interact with ecosystem features
       # counter for number of bits turned on i.e. number of 1's in the trait
        total_on = sum(trait.loci)
        return total_on/self.num_loci

    # ''' finds the how strong an individual's fitness is ''' #
    def find_fitness(self, eco_type):
        w = [] # fitness component matrix
        overall_fitness = 1
        theta = self.eco_type # an ecological niche
        x = self.genome.eco #first characteristic controls ecology
        for i in range(self.k):
            w.append(np.exp( ( ( -(self.convert(x[i]) - theta[i]) )**2 )/(2*self.sigma**2) ) )
            overall_fitness *= w[i]
        return overall_fitness

    # ''' finds how strongly an individual prefers a niche ''' #
    def find_preference(self, eco_type):
        p = [] # preference component matrix
        overall_pref = 1
        theta = eco_type # the set of environmental factors that together create an ecological niche
        y = self.genome.pref # second characteristic controls preference
        for i in range(self.k):
            if theta[i] == 1:
                p.append(.5 + .99*(self.convert(y[i]) - .5)) # where a[i] = .99 i.e. possible strength is .99, + when theta == 1
            else: # theta == 0
                p.append(.5 - .99*(self.convert(y[i]) - .5)) # where a[i] = .99 i.e. possible strength is .99, - when theta == 0
            overall_pref *= p[i]
        return overall_pref

    def is_species(self):
        for i in range(self.k):
            if sum(self.genome.eco[i].loci) != sum(self.genome.pref[i].loci):
                return False
            return True


    # ''' find the points at which we will perform crossover ''' #
    def find_crosspoints(self):
        cross_point1 = rand.randrange(self.k)
        cross_point2 = rand.randrange(self.k)
        while cross_point1 == cross_point2: # make sure the points are different
            cross_point2 = rand.randrange(self.k)
        if cross_point1 < cross_point2:
            return (cross_point1, cross_point2)
        else:
            return (cross_point2, cross_point1)
        
    def crossover(self, genome1, genome2):
        cross_point1, cross_point2 = self.find_crosspoints() # find the points at which we will do crossover
        # crossover pref and eco seperately
        for i in range(cross_point1, cross_point2+1): # inclusive,i.e if crosspoint is 2 to 3, it includes traits 2 and 3
            eco_chunk = genome1.eco[i] # save this 'chunk' so it doesn't get clobbered
            genome1.eco[i] = genome2.eco[i] # swap trait of genome2 into genome1
            genome2.eco[i] = eco_chunk  # swap trait of genome1 into genome2

            pref_chunk = genome1.pref[i] # same as above except for preference characteristic
            genome1.pref[i] = genome2.pref[i]
            genome2.pref[i] = pref_chunk


    def mutation(self, num_mutations): # use genomes of parents
        if num_mutations > 0:
            genome_length = self.genome_size()
            chosen = set() # so we get distinct numbers, and don't mutate the same bit twice!
            while len(chosen) != num_mutations:
                chosen.add(rand.randrange(genome_length)) # choose a random bit to 'mutate'
            bit_num = 0 # used to determine the 'number' of the bit
            self.mutate_traits(self.genome.eco, bit_num, chosen)
            self.mutate_traits(self.genome.pref, bit_num, chosen)


    def mutate_traits(self, characteristic, bit_num, chosen):
        for trait in range(len(characteristic)):
            for locus in range(trait):
                if bit_num in chosen: # if the bit we want to mutate is there
                    bit = characteristic[trait].loci[locus] # assign to variable for readability purposes
                    characteristic[trait].loci[locus] = not bit # locus = not locus
                    bit_num += 1
