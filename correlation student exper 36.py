import numpy as np

# Sample data: [study hours, exam scores]
study_hours = np.array([2, 3, 4, 5, 6])
exam_scores = np.array([70, 75, 80, 85, 90])

# Calculate correlation coefficient
correlation = np.corrcoef(study_hours, exam_scores)[0, 1]

print("Correlation between study hours and exam scores:", correlation)
