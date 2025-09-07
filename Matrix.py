import numpy as np
# Making special matrix

# 1. np.eye()
# for making an identity matrix
# 3x3 ki identity matrix
eye_mat = np.eye(3)
print(eye_mat)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 2. np.diag()
#  Ek 1D array se diagonal matrix banata hai, ya ek 2D matrix se diagonal elements nikalta hai.
# 1D array se diagonal matrix banana
diag_mat = np.diag([1, 5, 9])
print(diag_mat)
# [[1 0 0]
#  [0 5 0]
#  [0 0 9]]
