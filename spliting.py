# Spliting is breaking one large array into several smaller subarrays

# 1. np.split()
# either we can split into N equal subarrys or at specific points , using this function

# np.split(array,indices_or_sections,axis=0)
import numpy as np
arr = np.arange(12).reshape(4, 3)
print("Original Array:\n", arr)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# Split the array into 2 smaller arrays along rows (axis=0)
# This splits the 4 rows into two arrays of 2 rows each.
result_rows = np.split(arr, 2, axis=0)
print("Split into 2 arrays by row:\n", result_rows)
# [array([[0, 1, 2],
#         [3, 4, 5]]),
#  array([[6, 7, 8],
#         [9, 10, 11]])]

# Split the array into 3 smaller arrays along columns (axis=1)
# This splits the 3 columns into three arrays of 1 column each.
result_cols = np.split(arr, 3, axis=1)
print("\nSplit into 3 arrays by column:\n", result_cols)
# [array([[0], [3], [6], [9]]),
#  array([[1], [4], [7], [10]]),
#  array([[2], [5], [8], [11]])]

# spliting at specific points
arr1d = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]

# Split the 1D array at indices 3 and 7
# This creates three arrays: arr[:3], arr[3:7], and arr[7:]
result_points = np.split(arr1d, [3, 7])
print("Split at specific points:\n", result_points)
# [array([0, 1, 2]), array([3, 4, 5, 6]), array([7, 8, 9])]


## we can also use helper function vsplit and hsplit
# np.vsplit()

# Split the array into 2 parts vertically (by row)
vsplit_result = np.vsplit(arr, 2)
print("vsplit result:\n", vsplit_result)
# [array([[0, 1, 2],
#         [3, 4, 5]]),
#  array([[6, 7, 8],
#         [9, 10, 11]])]


# np.hsplit()

# Split the array into 3 parts horizontally (by column)
hsplit_result = np.hsplit(arr, 3)
print("\nhsplit result:\n", hsplit_result)
# [array([[0],[3],[6],[9]]),
#  array([[1],[4],[7],[10]]),
#  array([[2],[5],[8],[11]])]
