import numpy as np
import scipy.stats as stats

data = np.loadtxt("rare_elements.csv")  # One column of values

# Example: 95% confidence interval
mean = np.mean(data)
sem = stats.sem(data)
ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)

print("Mean concentration:", mean)
print("95% Confidence Interval:", ci)
