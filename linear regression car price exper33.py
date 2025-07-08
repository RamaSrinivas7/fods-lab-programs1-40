from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: [engine_size (L), mileage (k miles)]
X = np.array([
    [2.0, 50],
    [3.0, 30],
    [1.5, 70],
    [2.5, 40],
    [3.5, 20]
])

# Corresponding car prices
y = np.array([15000, 20000, 12000, 18000, 25000])

# Create the model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Predict price for a new car
new_car = np.array([[2.2, 45]])  # engine size=2.2L, mileage=45k miles
predicted_price = model.predict(new_car)

print("Predicted car price: $", predicted_price[0])
