from __future__ import division
import numpy as np
import random as rand
from trait import Trait

class Genome:
    def __init__(self, k, num_loci):	
        self.pref = [] # preference characteristics
        self.eco = [] # ecological characteristics
        self.k = k
        self.generate(num_loci)
        self.chars = (self.pref, self.eco) #characteristics in a tuple
        self.length = len(self.chars)

    def generate(self, num_loci):
        for i in range(self.k): # randomly choose a niche and whether it is "on" or "off"
            #self.eco.append([]) # the 2k characteristics; ecological and preference
            #self.pref.append([])
            self.eco.append(Trait(num_loci))
            self.pref.append(Trait(num_loci))