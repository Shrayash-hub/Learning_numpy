import numpy as np

# A sample array with distinct values
arr = np.arange(10, 101, 10) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Our Array:\n", arr)

# lets you access multiple array elements at once using an array of indices (or a list), rather than a single number or a slice.

# usefull for selecting non swquential elements

# Select the elements at index 2, 5, and 8
indices = [2, 5, 8]
print(arr[indices])
# Output: [30 60 90]

# You can even select the same element multiple times
indices = np.array([[1, 2], [4, 6]])
print(arr[indices])
# The output shape (2,2) matches the index array's shape
# [[20 30]
#  [50 70]]


# IN 2d ARRAYS

arr2d = np.arange(1, 13).reshape(4, 3)
print("2D Array:\n", arr2d)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# You can even select the same element multiple times
indices = np.array([[1, 2], [4, 6]])
print(arr[indices])
# The output shape (2,2) matches the index array's shape
# [[20 30]
#  [50 70]]

#Selecting Specific Rows
#You can pass a list of row numbers to get a new array with just those rows.

# Select the first, third, and fourth rows (indices 0, 2, 3)
print(arr2d[[0, 2, 3]])
# [[ 1  2  3]
#  [ 7  8  9]
#  [10 11 12]]


# Selecting Specific Elements (Row & Column Pairs)
# You can provide one array for the row indices and another for the column indices. This will select elements based on (row, column) pairs.


# Select elements at (0, 1), (2, 2), and (3, 0)
rows = np.array([0, 2, 3])
cols = np.array([1, 2, 0])

print(arr2d[rows, cols])
# Output: [ 2  9 10]

# how output came

# arr2d[rows[0], cols[0]] -> arr2d[0, 1] -> 2

# arr2d[rows[1], cols[1]] -> arr2d[2, 2] -> 9

# arr2d[rows[2], cols[2]] -> arr2d[3, 0] -> 10
