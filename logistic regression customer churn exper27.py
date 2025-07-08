from sklearn.linear_model import LogisticRegression

# Sample data: [usage_minutes, contract_length]
X = [[100, 12], [300, 24], [150, 6], [400, 36]]
y = [0, 1, 0, 1]  # 0: not churned, 1: churned

model = LogisticRegression()
model.fit(X, y)

new_customer = [[250, 12]]
print("Will Churn?", model.predict(new_customer))
