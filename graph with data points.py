import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the base volume of water
V_base = 0.25 # m^3

# Define the range of base densities to test
base_densities = [1000, 1150, 1300, 1450, 1600, 1750, 1900]  # kg/m^3  # kg/m^3

# Define the range of temperatures to test
temperatures = [-10, 30, 50, 70]  # Celsius

# Define the number of trials to run
num_trials = 10

# Calculate the buoyant force for each combination of base density and temperature
results = []
for rho in base_densities:
    row = []
    for temp in temperatures:
        # Initialize a list to store the results of each trial
        trial_results = []

        # Run the experiment for the specified number of trials
        for i in range(num_trials):
            # Calculate the mass of water
            m = rho * V_base

            # Add a random perturbation to the temperature
            perturbation = random.uniform(-1, 1)  # Celsius
            temp_perturbed = temp + perturbation

            # Calculate the density of water at the perturbed temperature
            rho_t = rho / (1 - ((temp_perturbed - 20) * 0.00021))

            # Calculate the buoyant force
            g = 9.81  # m/s^2
            F = rho_t * V_base * g

            # Add the result to the list of trial results
            trial_results.append((rho, temp, F))

        # Add the trial results to the row
        row.append(trial_results)

    # Add the row to the results
    results.append(row)

# Convert the results to a list of (x, y, z) tuples
data = []
for i in range(len(base_densities)):
    for j in range(len(temperatures)):
        for k in range(num_trials):
            (rho, temp, F) = results[i][j][k]
            data.append((rho, temp, F))

# Convert the data to numpy arrays
data = np.array(data)
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Create the 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# Add text to the data points
for i in range(len(data)):
    ax.text(data[i, 0], data[i, 1], data[i, 2], '%.2f' % data[i, 2], size=10, zorder=1, color='k')

# Set the axis labels
ax.set_xlabel('Base density (kg/m^3)')
ax.set_ylabel('Temperature (C)')
ax.set_zlabel('Buoyant force (N)')

# Show the plot
plt.show()
