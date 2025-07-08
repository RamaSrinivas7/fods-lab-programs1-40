import pandas as pd

# Sample data
order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2],
    'order_date': pd.to_datetime(['2025-06-01', '2025-06-02', '2025-06-05', '2025-06-06', '2025-06-07']),
    'product': ['A', 'B', 'A', 'C', 'B'],
    'quantity': [2, 1, 3, 4, 2]
})

# 1. Total orders per customer
orders_per_customer = order_data.groupby('customer_id').size()

# 2. Average quantity per product
avg_quantity = order_data.groupby('product')['quantity'].mean()

# 3. Earliest and latest order dates
earliest = order_data['order_date'].min()
latest = order_data['order_date'].max()

print("Orders per customer:\n", orders_per_customer)
print("Average quantity per product:\n", avg_quantity)
print("Earliest:", earliest, "| Latest:", latest)
