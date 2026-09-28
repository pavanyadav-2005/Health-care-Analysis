import numpy as np

ages = np.array([0.19,0.22,0.27,0.32,0.37,0.42,0.47,0.52,0.57,0.62,0.67,0.72])

print("Patient Ages:", ages)

print("Average Age:", np.mean(ages))
print("Minimum Age:", np.min(ages))
print("Maximum Age:", np.max(ages))
print("Total Age:", np.sum(ages))
print("Standard Deviation:", np.std(ages))