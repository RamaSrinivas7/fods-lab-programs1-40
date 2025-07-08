import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
temperature = [30, 32, 35, 33]
rainfall = [80, 60, 120, 90]

# Line Plot - Temperature
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter Plot - Rainfall
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
