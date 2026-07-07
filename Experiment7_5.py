import numpy as np

scores = np.array([
    [85, 92, 78, 90],
    [91, 88, 95, 86],
    [76, 65, 80, 72],
    [88, 94, 89, 93],
    [82, 79, 85, 81]
])

print("Original scores:\n", scores)

# Per-course statistics
course_avg = np.mean(scores, axis=0)
course_max = np.max(scores, axis=0)
course_min = np.min(scores, axis=0)
print("\nPer-course average:", course_avg)
print("Per-course highest:", course_max)
print("Per-course lowest:", course_min)

# Per-student total and average
student_total = np.sum(scores, axis=1)
student_avg = np.mean(scores, axis=1)
print("\nPer-student total:", student_total)
print("Per-student average:", student_avg)

# Find all scores >= 90
high_scores = scores[scores >= 90]
print("\nScores >= 90:", high_scores)

# Replace scores < 60 with 60
scores[scores < 60] = 60
print("\nAfter replacing <60 with 60:\n", scores)

# Sort descending by first column (Chinese scores)
sorted_indices = np.argsort(scores[:, 0])[::-1]  # descending order
sorted_scores = scores[sorted_indices]
print("\nSorted by Chinese scores (descending):\n", sorted_scores)
