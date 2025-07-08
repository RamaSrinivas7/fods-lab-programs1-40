# Product base price
price = 100  

# Discount and tax percentages
discount_percent = 10
tax_percent = 5

# Apply discount
discounted_price = price - (price * discount_percent / 100)

# Apply tax on discounted price
total_cost = discounted_price + (discounted_price * tax_percent / 100)

print("Total Cost after discount and tax:", total_cost)
