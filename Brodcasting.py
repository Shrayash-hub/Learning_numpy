import numpy as np

# Brodcasting is the set of rules NumPy follows to perform vectorized operations on arrays of different but compatible shapes

# adding a scaler to array or adding 1d array to 2d array without manual reshaping

### RULES OF BRODCASTING

# 1. If the arrays have a different number of dimensions, the shape of the smaller array is padded with 1s on its left side.

# 2. If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is "stretched" to match the other shape.

""" imagine the shapes of two arrays, A and B.

Array A ka shape hai: (4, 3)

Array B ka shape hai: (3,) 


adjust the shapes from right side:

Array A ka shape:   4 x 3
Array B ka shape:       3

by rule 1: add 1

Array A ka shape:   4 x 3
Array B ka shape:   1 x 3  (aage 1 lag gaya)

by rule 2: check every dimension from right -> compare
           dimensions are compatible if:
           any of dimension have same number like 3 in both
           or any of one dimension have 1, like 1 in second dimension
streach the dimesion having 1 toh 4*3 from 1*3
"""

# 3. If in any dimension the sizes disagree and neither is equal to 1, a ValueError is raised. ( har dimension k liye compare krna  h)

arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

# Broadcasting the scalar to the array
result = arr + scalar
print(result)
# [[11 12 13]
#  [14 15 16]]



matrix = np.arange(6).reshape(2, 3) # Shape (2, 3)
vector = np.array([10, 20, 30])      # Shape (3,)

result = matrix + vector
# [[0 1 2]    +    [10 20 30]
# [3 4 5]]         [10 20 30]
print(result)
# [[10 21 32]
#  [13 24 35]]
