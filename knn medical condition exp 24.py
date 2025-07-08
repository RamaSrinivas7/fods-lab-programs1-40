from sklearn.neighbors import KNeighborsClassifier

# Sample data
X = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]  # 0: No condition, 1: Has condition

# Train KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predict for a new patient
new_patient = [[4, 4]]
print("Predicted Condition:", knn.predict(new_patient))
