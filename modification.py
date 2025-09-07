# 1. Inserting the elements np.insert()

# It returns a new array with the specified values inserted at a given position.
# np.insert(array, index, values, axis=None

## insertion in 1D Array

import numpy as np

arr1d = np.array([10, 20, 30, 40])

# Insert a single value (99) at index 2
new_arr1 = np.insert(arr1d, 2, 99)
print("Insert single value:\n", new_arr1)
# Output: [10 20 99 30 40]

# Insert multiple values at a single index
new_arr2 = np.insert(arr1d, 2, [99, 88])
print("\nInsert multiple values:\n", new_arr2)
# Output: [10 20 99 88 30 40]


## insertion in 2D arrays

# axis parameter is crucial -> wheather to insert a new row or a new clm

arr2d = np.array([[1, 2], [3, 4]])

# If axis is not specified, the array is flattened first
flat_insert = np.insert(arr2d, 2, 99)
print("Insertion with axis=None (flattened):\n", flat_insert)
# Output: [ 1  2 99  3  4]

# Insert a new ROW at index 1 (axis=0)
row_to_insert = [99, 88]
new_row_arr = np.insert(arr2d, 1, row_to_insert, axis=0)
print("\nInsert a new row (axis=0):\n", new_row_arr)
# [[ 1 99]
#  [ 2 88]
#  [ 3  4]]

# Insert a new COLUMN at index 1 (axis=1)
col_to_insert = [99, 88]
new_col_arr = np.insert(arr2d, 1, col_to_insert, axis=1)
print("\nInsert a new column (axis=1):\n", new_col_arr)
# [[ 1 99  2]
#  [ 3 88  4]]



# 2. np.append()
# insertion at the very end of the arrays, also returns a new array

# Append to a 1D array
appended_arr = np.append(arr1d, [50, 60])
print("Appended 1D:\n", appended_arr)
# Output: [10 20 30 40 50 60]

# Append a new row to a 2D array (requires axis=0)
row_to_append = [[5, 6]] # Must have the same number of dimensions
appended_2d = np.append(arr2d, row_to_append, axis=0)
print("\nAppended 2D:\n", appended_2d)
# [[1 2]
#  [3 4]
#  [5 6]]


# 3. conatenation : np.concatenate()
# joining multiple arrays into a single, larger array. This is a fundamental operation for combining datasets.

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# concatinating the rows ( axis = 0 )

# Stacking vertically
row_concat = np.concatenate((a, b), axis=0)
print("Row concatenation (axis=0):\n", row_concat)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# concatinating the clms ( axis = 1)

# Stacking horizontally
col_concat = np.concatenate((a, b), axis=1)
print("\nColumn concatenation (axis=1):\n", col_concat)
# [[1 2 5 6]
#  [3 4 7 8]]

## we can also use functions like vstack() and hstack() to stack them vertically and horizontally

v_stack = np.vstack((a, b))
print("vstack result:\n", v_stack)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

h_stack = np.hstack((a, b))
print("\nhstack result:\n", h_stack)
# [[1 2 5 6]
#  [3 4 7 8]]

# 4. np.delete()
# np.delete(array, index, axis = None)
# Delete the element at index 2 from arr1d
deleted_arr = np.delete(arr1d, 2)
print("Deleted 1D:\n", deleted_arr)
# Output: [10 20 40]

# Delete the second row (index 1) from arr2d
deleted_row = np.delete(arr2d, 1, axis=0)
print("\nDeleted row:\n", deleted_row)
# [[1 2]]




