from sklearn.linear_model import LinearRegression

# Sample house data: [area, bedrooms]
X = [[1000, 2], [1500, 3], [2000, 4]]
y = [200000, 300000, 400000]  # prices

model = LinearRegression()
model.fit(X, y)

new_house = [[1800, 3]]
print("Predicted Price:", model.predict(new_house))
