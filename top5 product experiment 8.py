import pandas as pd

# Sample sales data
sales_data = pd.DataFrame({
    'product': ['A', 'B', 'C', 'A', 'B', 'A'],
    'quantity': [5, 3, 2, 6, 4, 5]
})

# Group by product and sum quantities
top_products = sales_data.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)

print("Top 5 Sold Products:\n", top_products)
