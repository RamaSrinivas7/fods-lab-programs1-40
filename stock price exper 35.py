import numpy as np

# Sample data: closing prices over 5 days
closing_prices = np.array([150, 155, 160, 158, 162])

# Calculate the daily price changes
price_changes = np.diff(closing_prices)

# Calculate average change
average_change = np.mean(price_changes)

print("Average daily price change:", average_change)
