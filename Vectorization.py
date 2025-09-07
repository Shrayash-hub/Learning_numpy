# Vectorization is the practice of performing operations on entire arrays

"""
Benefits of Vectorization
1. Speed: As shown, it provides massive performance gains.

2. Readability: Vectorized code is more concise and easier to understand. c = a + b is much cleaner than writing a full for loop.

3. Fewer Bugs: Less code means fewer chances for errors, like mistakes in loop indexing.

"""

import numpy as np
import time

# Create two large arrays
arr1 = np.arange(1_000_000)
arr2 = np.arange(1_000_000)

# --- Method 1: Python Loop (Non-Vectorized) ---
start_time = time.time()
result_loop = np.zeros(1_000_000)
for i in range(len(arr1)):
    result_loop[i] = arr1[i] + arr2[i]
end_time = time.time()
print(f"Time with Python loop: { (end_time - start_time) * 1000:.2f} ms")

# --- Method 2: NumPy (Vectorized) ---
start_time = time.time()
result_numpy = arr1 + arr2
end_time = time.time()
print(f"Time with Vectorization: { (end_time - start_time) * 1000:.2f} ms")