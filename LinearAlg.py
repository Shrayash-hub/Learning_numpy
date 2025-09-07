import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Dot Product (Matrix Multiplication)
# Ye element-wise multiplication nahi hai!
print("Dot product:\n", a @ b)
# or np.dot(a, b)

# Transpose of array(rows ko columns banana)
print("Transpose of a:\n", a.T)