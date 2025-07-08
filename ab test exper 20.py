from scipy import stats

# Sample data: conversions
design_a = [0.15, 0.17, 0.16, 0.14, 0.18]
design_b = [0.10, 0.12, 0.11, 0.13, 0.09]

t_stat, p_value = stats.ttest_ind(design_a, design_b)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Statistically significant difference.")
else:
    print("No statistically significant difference.")
