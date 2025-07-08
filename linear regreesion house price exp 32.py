from sklearn.linear_model import LinearRegression
import numpy as np

# Example data: features (e.g., size, number of bedrooms) and target (price)
X = np.array([[1500, 3], [2000, 4], [1700, 3], [2500, 4], [1600, 2]])
y = np.array([300000, 400000, 350000, 500000, 320000])

# Create the linear regression model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Predict house price for a new house
new_house = np.array([[1800, 3]])  # size=1800 sq ft, 3 bedrooms
predicted_price = model.predict(new_house)

print("Predicted house price: $", predicted_price[0])
