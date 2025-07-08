import numpy as np

# 4x4 matrix: rows = students, columns = subjects (Math, Science, English, History)
student_scores = np.array([
    [85, 90, 75, 88],
    [78, 92, 80, 85],
    [90, 85, 85, 82],
    [88, 76, 79, 90]
])

# Calculate average per subject (column-wise)
subject_avg = np.mean(student_scores, axis=0)

# Find subject with highest average
highest_subject_index = np.argmax(subject_avg)

# Subject names
subjects = ['Math', 'Science', 'English', 'History']

print("Average score per subject:", subject_avg)
print("Subject with highest average score:", subjects[highest_subject_index])
