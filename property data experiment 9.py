import pandas as pd

# Sample property data
property_data = pd.DataFrame({
    'location': ['X', 'Y', 'X', 'Z', 'Y'],
    'bedrooms': [3, 5, 6, 2, 4],
    'area': [1500, 2200, 2500, 1400, 1800],
    'price': [300000, 500000, 550000, 250000, 400000]
})

# 1. Number of properties with > 4 bedrooms
more_than_4 = property_data[property_data['bedrooms'] > 4].shape[0]

# 2. Average price by location
avg_price = property_data.groupby('location')['price'].mean()

# 3. Property with largest area
largest_property = property_data.loc[property_data['area'].idxmax()]

print("Properties with > 4 bedrooms:", more_than_4)
print("Average price by location:\n", avg_price)
print("Property with largest area:\n", largest_property)
