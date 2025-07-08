import matplotlib.pyplot as plt

# Sample sales data
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [100, 150, 120, 180]

# Line Plot
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar Plot
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
