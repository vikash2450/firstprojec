import numpy as np  # Step 1: Import the NumPy library
indices = np.indices((8, 6))

sum_indices = indices[0] + indices[1]


matrix = sum_indices % 2


print(matrix)
