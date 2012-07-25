from __future__ import division
import numpy as np
import random as rand

class Trait:
    def __init__(self, num_loci):
        self.length = num_loci
        self.loci = self.generate()

    def generate(self):
        trait_bit = True # all inds start with traits at 1/2 (homozygotes)
        loci = []
        for i in range(self.length): # randomly choose a niche and whether it is "on" or "off"
            loci.append(trait_bit)
            trait_bit = not trait_bit
        return loci