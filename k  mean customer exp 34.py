from sklearn.cluster import KMeans
import numpy as np

# Sample data: [average spending, number of visits]
X = np.array([
    [100, 10],
    [200, 20],
    [150, 15],
    [300, 25],
    [400, 30]
])

# Number of segments
k = 2

# Create and fit KMeans
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Assign each customer to a segment
print("Customer segments:", kmeans.labels_)
