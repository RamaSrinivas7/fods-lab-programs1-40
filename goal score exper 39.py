import pandas as pd

# Load data from CSV file
df = pd.read_csv('players.csv')

# Find top 5 players with most goals
top_goals = df.nlargest(5, 'Goals')
print("Top goal scorers:\n", top_goals)

# Find top 5 players with highest salaries
top_salaries = df.nlargest(5, 'Salary')
print("Highest paid players:\n", top_salaries)
