import numpy as np
from sklearn.cluster import KMeans

# Sample data: total spent and number of transactions
X = np.array([
    [100, 5],
    [200, 12],
    [150, 7],
    [300, 18],
    [400, 20]
])

# Create and fit K-Means with 2 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Print cluster assignments
print("Customer segments:", kmeans.labels_)
