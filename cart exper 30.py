from sklearn.tree import DecisionTreeRegressor

# Sample car data: [mileage, age]
X = [[30000, 2], [50000, 4], [70000, 5]]
y = [400000, 300000, 200000]

model = DecisionTreeRegressor()
model.fit(X, y)

new_car = [[60000, 3]]
print("Predicted Car Price:", model.predict(new_car))
