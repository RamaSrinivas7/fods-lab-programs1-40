import pandas as pd

data = pd.DataFrame({'likes': [10, 20, 10, 30, 10, 20, 40]})
like_freq = data['likes'].value_counts()

print("Likes Frequency:\n", like_freq)
