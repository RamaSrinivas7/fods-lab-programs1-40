import pandas as pd
from scipy import stats

# Example data
data = pd.DataFrame({
    'group': ['drug']*5 + ['placebo']*5,
    'effect': [12, 13, 11, 14, 15, 5, 6, 7, 6, 5]
})

drug = data[data['group'] == 'drug']['effect']
placebo = data[data['group'] == 'placebo']['effect']

# T-test
t_stat, p_value = stats.ttest_ind(drug, placebo)

print("T-stat:", t_stat)
print("P-value:", p_value)
