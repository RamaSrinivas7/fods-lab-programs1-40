import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [100, 150, 120, 180]

# 1. Line Plot
plt.plot(months, sales)
plt.title("Line Plot")
plt.show()

# 2. Scatter Plot
plt.scatter(months, sales)
plt.title("Scatter Plot")
plt.show()

# 3. Bar Plot
plt.bar(months, sales)
plt.title("Bar Plot")
plt.show()
