from sklearn.cluster import KMeans

# Sample shopping behavior: [spending score, income]
X = [[15, 40], [16, 42], [70, 150], [72, 140], [20, 45], [68, 160]]

model = KMeans(n_clusters=2)
model.fit(X)

new_customer = [[18, 44]]
print("Customer Segment:", model.predict(new_customer))
