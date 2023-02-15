# Define the base volume of water
V_base = 0.25# m^3

# Define the range of base densities to test
base_densities = [1000, 1150, 1300, 1450, 1600, 1750, 1900]  # kg/m^3

# Define the range of temperatures to test
temperatures = [-10, 30, 50, 70]  # Celsius

# Calculate the buoyant force for each combination of base density and temperature
results = []
for rho in base_densities:
    row = []
    for temp in temperatures:
        # Calculate the mass of water
        m = rho * V_base

        # Calculate the density of water at the given temperature
        rho_t = rho / (1 - ((temp - 20) * 0.00021))

        # Calculate the buoyant force
        g = 9.81  # m/s^2
        F = rho_t * V_base * g

        row.append(F)
    results.append(row)

# Print the results as a table
print("Buoyant force (N)")
print("Base density (kg/m^3) \ Temperature (C) | ", end="")
for temp in temperatures:
    print("{:6d}   |".format(temp), end="")
print("")
print("-" * 43)
for i in range(len(base_densities)):
    print("{:17d} | ".format(base_densities[i]), end="")
    for j in range(len(temperatures)):
        print("{:10.2f} |".format(results[i][j]), end="")
    print("")
