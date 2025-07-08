import numpy as np

# Sample temperature data: each row is a city, columns are days
temperatures = np.array([
    [20, 22, 19, 24],  # City 1
    [25, 27, 26, 28],  # City 2
    [18, 20, 19, 21]   # City 3
])

# Calculate mean temperature for each city
mean_temps = np.mean(temperatures, axis=1)

# Find city with highest temperature range
temp_range = np.ptp(temperatures, axis=1)  # peak-to-peak (max-min)
max_range_city = np.argmax(temp_range)

print("Mean temperatures:", mean_temps)
print("City with highest temperature range:", max_range_city + 1)
