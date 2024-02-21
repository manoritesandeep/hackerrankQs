import numpy as np

arr = np.array([3, 1, 2])

# Using np.argsort()
sorted_indices = np.argsort(arr)
sorted_arr_using_indices = arr[sorted_indices]

print(sorted_indices)  # Output: [1 2 0]
print(sorted_arr_using_indices)  # Output: [1 2 3]

# Using np.sort()
sorted_arr = np.sort(arr)

print(sorted_arr)  # Output: [1 2 3]
