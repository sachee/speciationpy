class Parameters:
	def __init__(self):
		self.SIGMA = .356 # as in the paper
		self.MAX_CAP = 500  # carrying capacity
		self.num_env_fac = 3 # number of environmental factors which determine ecological niches
		self.grid_size = 4 # size of environment, an NxN grid
		self.num_loci = 3 # number of loci for a trait
		self.dispersion_radius = 1 # how many squares inds can migrate in one migration
		self.b = 4 # average number of offspring per female
		self.mutation_rate = 5 # 10^-5
		self.extinction_rate = .0025