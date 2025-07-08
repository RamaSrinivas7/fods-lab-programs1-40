import numpy as np
import scipy.stats as stats

# Example data
drug = np.array([10, 12, 11, 13, 14])
placebo = np.array([5, 7, 6, 8, 7])

def confidence_interval(data):
    mean = np.mean(data)
    sem = stats.sem(data)
    interval = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)
    return interval

print("95% CI for drug:", confidence_interval(drug))
print("95% CI for placebo:", confidence_interval(placebo))
