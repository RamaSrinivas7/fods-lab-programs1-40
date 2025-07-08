import numpy as np

# Each row is a product, each column is a week's price
sales_data = np.array([
    [100, 150, 200],
    [120, 130, 180],
    [90, 160, 170]
])

# Calculate average price for each product (row-wise)
average_prices = np.mean(sales_data, axis=1)

print("Average price per product:", average_prices)
