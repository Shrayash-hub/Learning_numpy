import numpy as np

arr = np.arange(1, 13) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print("Original Array (shape", arr.shape, "):\n", arr)

# .reshape() : changes the shape of the array , without changing the original data

# Reshape the 1D array into a 3x4 matrix (3 rows, 4 columns)
reshaped_arr = arr.reshape(3, 4)
print("Reshaped Array (3, 4):\n", reshaped_arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# rule : number of elements must remain same
# The -1 Trick: You can let NumPy automatically calculate one of the dimensions by passing -1. This is extremely useful.

# Reshape into a matrix with 4 rows, and let NumPy figure out the columns
arr_auto = arr.reshape(4, -1)
print("Reshaped with -1 (4, 3):\n", arr_auto)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]



# FLATTENING THE ARRAYS : multidimensional to 1d array

# 1: ravel():  returns a view of the original array whenever possible. It's faster because doesn't create new data in memory. Modifying the raveled array will modify the original.
# Start with our reshaped 3x4 array
reshaped_arr = arr.reshape(3, 4)

# Using ravel() (a view)
raveled_arr = reshaped_arr.ravel()
raveled_arr[0] = 99 # Modify the raveled array

print("Original array after modifying raveled view:\n", reshaped_arr)
# [[99  2  3  4]  <- Original array is changed
#  [ 5  6  7  8]
#  [ 9 10 11 12]]


# 2. flatten(): returns a copy of the data , safe

# Using flatten() (a copy)
flattened_arr = reshaped_arr.flatten()
flattened_arr[1] = 777 # Modify the flattened copy

print("\nOriginal array after modifying flattened copy:\n", reshaped_arr)
# [[99  2  3  4]  <- Original array is NOT changed
#  [ 5  6  7  8]
#  [ 9 10 11 12]]