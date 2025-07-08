from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target

# Train decision tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
print("Predicted species:", model.predict(new_flower))
