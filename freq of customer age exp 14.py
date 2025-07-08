import pandas as pd
from collections import Counter

data = pd.DataFrame({'age': [25, 30, 25, 40, 30, 25, 35]})
age_freq = data['age'].value_counts()

print("Age Frequency:\n", age_freq)
