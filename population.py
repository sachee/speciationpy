# Sasha Solomon #
# 6/18/2012     #
# Speciation    #

from __future__ import division
import numpy as np
from individual import Individual

class Population:
    def __init__(self):
        self.members = []
        self.size = 0

    def initial_pop(self, carry_cap, loci, num_env_fac, eco_type, SIGMA):
        for _ in range(carry_cap):
            ind = Individual(loci, num_env_fac, eco_type, SIGMA)
            self.members.append(ind)

    def selection(self):
        # stuff here
        return 0
