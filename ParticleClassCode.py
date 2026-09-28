import numpy as np

## 2. Start by creating a particle class. This class should store information about our particles,
## including mass, position, and velocity (though we won’t use velocity for right now since we’ll
## be picturing the particles as fixed in their locations). We can then create an array of particles
## that will make it easier to compute the potential.

class Particle:
    def __init__(self, mass_particle, position_x, position_y, position_z):

        ## Stores mass
        self.mass_particle = mass_particle

        ## Store position coordinates (e.g., [x, y, z])
        self.position_x = position_x ## The Position on the X-axis

        self.position_y = position_y ## The Position on the Y-axis

        self.position_z = position_z ## The Position on the Z-axis