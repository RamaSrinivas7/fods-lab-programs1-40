import pandas as pd

# Load stock data from a CSV file
data = pd.read_csv('stock_data.csv')

# Calculate daily price changes
data['Price Change'] = data['Close'].diff()

# Display the date, close price, and daily change
print(data[['Date', 'Close', 'Price Change']])
