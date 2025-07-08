from sklearn.cluster import KMeans
import numpy as np

# Sample customer data: [age, income]
customer_data = np.array([
    [25, 50000],
    [35, 60000],
    [45, 80000],
    [23, 52000],
    [40, 78000],
    [30, 62000]
])

# Number of segments needed
k = 2

# Create KMeans model
kmeans = KMeans(n_clusters=k)
# Fit the model
kmeans.fit(customer_data)

# Output the cluster each customer belongs to
print("Customer segments:", kmeans.labels_)
