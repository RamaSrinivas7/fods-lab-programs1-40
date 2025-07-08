import numpy as np

# Fuel efficiency (miles per gallon) for two car models
fuel_efficiency = np.array([25, 30])  # Car 1: 25 mpg, Car 2: 30 mpg

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate percentage improvement from Car 1 to Car 2
percentage_improvement = ((fuel_efficiency[1] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Average Fuel Efficiency:", average_efficiency)
print("Percentage Improvement:", percentage_improvement, "%")
