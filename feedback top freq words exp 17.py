import pandas as pd
from collections import Counter
import re

# Load CSV
data = pd.read_csv('data.csv')  # Contains column "feedback"

# Preprocess
def preprocess(text):
    words = re.findall(r'\b\w+\b', text.lower())
    stopwords = {'the', 'is', 'and', 'a', 'an', 'to'}
    return [word for word in words if word not in stopwords]

all_words = []
for feedback in data['feedback']:
    all_words.extend(preprocess(str(feedback)))

# Frequency distribution
word_freq = Counter(all_words)

# Top N words
N = 5
top_n = word_freq.most_common(N)
print("Top", N, "Words:\n", top_n)
