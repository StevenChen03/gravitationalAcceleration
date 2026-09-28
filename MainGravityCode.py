import ParticleClassCode as PCC
import numpy as np
import matplotlib.pyplot as plt ## Used for creating graphs

## Constants

G = 6.67E-11 ## Newton's Gravity Constant

## Arraies in Main File
particles_array_small = []
particles_array_large =[]

## Opening the two files and reasing all variables into the array.
particle_sample_small = np.loadtxt("particlesSmallGA.txt")

for particle in particle_sample_small:
    particle_small = PCC.Particle(particle[3], particle[0], particle[1], particle[2])
    particles_array_small.append(particle_small)

particle_sample_large = np.loadtxt("particlesLargeGA.txt")

for particle in particle_sample_large:
    particle_large = PCC.Particle(particle[3], particle[0], particle[1], particle[2])
    particles_array_large.append(particle_large)

## You can now easily loop through this array to compute the potential at any point
print(f"Successfully created an array with {len(particles_array_small)} fixed small particles.")
print("\n")
print(f"Successfully created an array with {len(particles_array_large)} fixed large particles.")


## 3. In your main program file, start by writing a function which can take the list of particles and a
## position and return the potential at that point. Some pseudocode of this would be:
##
## define gravPotential(pos, particles)
## phi = 0.0
## for each particle p
## r = sqrt((p.x - pos.x)^2 + (p.y - pos.y)^2 + (p.z - pos.z)^2)
## phi += -G*p.mass/r
## return phi

def gravPotential(pos, particles):
    phi = 0.0
    for particle in particles:
        r = np.sqrt((particle.position_x - pos[0])**2 + (particle.position_y - pos[1])**2 + (particle.position_z - pos[2])**2)
        phi += -G*(particle.mass_particle)/r

    return phi

## 4. Setup your code to read in a provided list of particle positions and masses and create an array
## of these particles.

## THe Arrays are at the beginning of this code

## 5. Note that we will need three-dimensional positions for this, so we might need to create another
## derivative function to handle that case. Additionally, we will need to be able to pass our list of
## particles to the potential function, The pseudocode for this central difference when dealing
## with three dimensional data would be
##
## define centralDifferenceGrav3D(f, position, h, i, particles):
## x_1 = position with h/2 subtracted from coordinate at index i
## x_2 = position with h/2 added to coordinate at index i
## return (f(x_2, particles) - f(x_1, particles))/h
##
## There are other ways of setting up code so that we could use more generalized functions, but
## it should be more straightforward for now to simply write this specialized function.

def centralDifferenceGrav3D(f, position, h, i, particles):
    x_1 = []
    for j, component in enumerate(position):
        if (j != i):
            x_1.append(component)
        else:
            x_1.append(component - h/2)
    
    x_2 = []
    for j, component in enumerate(position):
        if (j != i):
            x_2.append(component)
        else:
            x_2.append(component + h/2)
    
    return (f(x_2, particles) - f(x_1, particles))/h

## 6. Prompt the user for a position to compute the gravitational acceleration.

userposition_x = float(input("Enter the X-Coordinate Position: "))
userposition_y = float(input("Enter the Y-Coordinate Position: "))
userposition_z = float(input("Enter the Z-Coordinate Position: "))

## 7. Using the provided position, have your code compute the gradient of the potential at those
## coordinates and then print out the acceleration vector. Use this as a test case by using the small
## provided file to compute the gravitational acceleration at some point. Using your introductory
## physics knowledge, compute the value at that point “by hand” and then compare with your
## codes output. Once you are satisfied that your code is functioning properly, proceed to the
## next step.

g_acceleration_x = centralDifferenceGrav3D(gravPotential, [userposition_x, userposition_y, userposition_z], 0.0001, 0, particles_array_small)
g_acceleration_y = centralDifferenceGrav3D(gravPotential, [userposition_x, userposition_y, userposition_z], 0.0001, 1, particles_array_small)
g_acceleration_z = centralDifferenceGrav3D(gravPotential, [userposition_x, userposition_y, userposition_z], 0.0001, 2, particles_array_small)

print ("\n")
print (f"The gravitational acceleration in the X-direction is {g_acceleration_x: .20f} m/s^2")
print (f"The gravitational acceleration in the X-direction is {g_acceleration_y: .20f} m/s^2")
print (f"The gravitational acceleration in the X-direction is {g_acceleration_z: .20f} m/s^2")
print ("\n")


## 8. Using the provided file with the large number of particles, set up your code to compute the
## acceleration at each particles location. Make sure that you don’t include the self gravity of
## the particle itself. This can be done by making sure the separation is larger than ℎ/2 before
## adding in the effect to the gravitational potential at that point. Make sure that the code can run
## without having to input anything (you can just hard-code the file name and the positions are
## going to be taken from the particles list so you don’t need to prompt for them).

proceed = input ("Proceed to the calculations [Type 1 for YES or 2 (or anything else for that matter) for NO]: ?")

## Proceeding to the calculations

g_acceleration_large = []

if (proceed=="1"):
    print("\n")
    print ("Proceeding to calculations.")

    print ("\n")
    for particle in particles_array_large:
        g_acceleration_x = centralDifferenceGrav3D(gravPotential, [particle.position_x, particle.position_y, particle.position_z], 0.0001, 0, particles_array_large)
        g_acceleration_y = centralDifferenceGrav3D(gravPotential, [particle.position_x, particle.position_y, particle.position_z], 0.0001, 1, particles_array_large)
        g_acceleration_z = centralDifferenceGrav3D(gravPotential, [particle.position_x, particle.position_y, particle.position_z], 0.0001, 2, particles_array_large)

    print ("Concluding calculations of each particle.")


## Ending the program
else:
    print("\n")
    print ("Ending program.")

## 9. Time how long the code takes to execute. On Linux distributions and macOS you can simply
## prepend your execution command with time
##
## time python MainGravityCode.py
##
## and after the code executes, you will see information about how long it took. On Windows,
## you’ll have to execute the code in PowerShell (this is the terminal you will see in VS Code)
## and then prepend with
##
## Measure-Command { python MainGravityCode.py }
## 
## It took approximately 15 seconds for the program to analyze the large particles

## Creating the graph:

## 1. Input measured data
print("\n")
print ("It took approximately 15 seconds to execute the program.")
t_measured = 15 ## The time it took to execute the program in seconds
N_measured = 2048 ## The amount of particles in the large file.

## 2. Calculate the coefficient A
a = (t_measured)/(N_measured**2)
print (f"The Calculated scaling factor A is {a: .4e} seconds/particle^2"
)

# 3. Generate data points for the plot
N_values = np.linspace(0, 10000, 500)
t_values = a * (N_values**2)

# 4. Create the plot
plt.figure(figsize=(8, 5))
plt.plot(N_values, t_values, label=f'Model: $t(N) = {a:.2e} \\cdot N^2$', color='blue')
plt.scatter([N_measured], [t_measured], color='red', zorder=5, label=f'Measured ({N_measured} particles)')

plt.title('N-Body Simulation Time Scaling ($O(N^2)$)')
plt.xlabel('Number of Particles ($N$)')
plt.ylabel('Execution Time (seconds)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig("X_vs_Y_graph_for_QuadraticExecutionTimeComplexity.pdf")