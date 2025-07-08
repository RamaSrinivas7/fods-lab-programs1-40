import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Given data
age = [23, 27, 27, 22, 27, 32, 21, 25, 25, 24, 29, 28, 30, 23, 21, 26, 22, 31]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 25.7, 27.8, 24.6, 20.4, 27.3, 29.8, 26.0, 32.7, 34.2, 31.2, 31.2]

df = pd.DataFrame({'age': age, '%fat': fat})

# Mean, Median, Std
print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())

# Boxplot
sns.boxplot(data=df)
plt.title("Boxplot of Age and %Fat")
plt.show()

# Scatter plot
plt.scatter(df['age'], df['%fat'])
plt.title("Scatter Plot of Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.show()

# Q-Q plot
stats.probplot(df['%fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot of %Fat")
plt.show()
