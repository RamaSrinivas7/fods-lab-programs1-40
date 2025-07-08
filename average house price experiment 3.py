import numpy as np

# Each row = [bedrooms, square_footage, sale_price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2000, 400000],
    [6, 2200, 500000],
    [4, 1800, 300000]
])

# Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Get sale prices (column index 2)
sale_prices = filtered_houses[:, 2]

# Calculate average sale price
average_price = np.mean(sale_prices)

print("Average sale price (more than 4 bedrooms):", average_price)
