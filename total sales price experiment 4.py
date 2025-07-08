import numpy as np

# Quarterly sales: Q1, Q2, Q3, Q4
sales_data = np.array([20000, 25000, 30000, 40000])

# Total sales for the year
total_sales = np.sum(sales_data)

# Percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales for the Year:", total_sales)
print("Percentage Increase (Q1 to Q4):", percentage_increase, "%")
