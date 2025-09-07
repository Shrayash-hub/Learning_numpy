import numpy as np

# Our 1D Array (Vector)
arr1d = np.arange(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("1D Array:\n", arr1d)

# Our 2D Array (Matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# indexing means accessing a single element from the array using its position. 

# First element (at index 0)
print(arr1d[0]) # Output: 0

# Fourth element (at index 3)
print(arr1d[3]) # Output: 3

# Last element (can also be accessed with -1)
print(arr1d[-1]) # Output: 9 (going to give elements from last)


# First row, second column (value: 2)
print(arr2d[0, 1]) # Output: 2

# Third row, third column (value: 9)
print(arr2d[2, 2]) # Output: 9

# Second row, first column (value: 4)
print(arr2d[1, 0]) # Output: 4



# SLICING

# Slicing lets you extract a portion (a sub-array) of an array. The syntax is: arr[start:stop:step]

# start: The index where the slice begins (this index is included).

# stop: The index where the slice ends (this index is not included).

# step: The number of elements to skip between each element in the slice.

# Elements from index 2 to 5 (the 5th index is not included)
print(arr1d[2:5]) # Output: [2 3 4]

# From the beginning up to index 4
print(arr1d[:4]) # Output: [0 1 2 3]

# From index 5 to the end
print(arr1d[5:]) # Output: [5 6 7 8 9]

# Every second element in the entire array
print(arr1d[::2]) # Output: [0 2 4 6 8]

# For reversing the whole array
print(arr1d[::-1])


# IN 2D ARRAY

# arr[row_slice, column_slice]

# First two rows, and from column 1 to the end
# arr2d[0:2, 1:]
print(arr2d[:2, 1:])
# [[2 3]
#  [5 6]]

# Some Common 2D Slicing Examples:

# Getting a complete Row:

# All elements of the second row (index 1)
print(arr2d[1, :]) # Output: [4 5 6]
# This can also be written as arr2d[1]


#Getting a complete Column:

# All elements of the third column (index 2)
print(arr2d[:, 2]) # Output: [3 6 9]



# -------------IMPORTANT----------------

# When you slice an array, NumPy does not create a new array. It gives you a view, which is like a window into the original array's data.

# This means that if you modify the slice, the original array will also change!

# Let's create a slice of arr1d
my_slice = arr1d[3:6] # [3 4 5]
print("Original Slice:", my_slice)

# Now let's change the first value of the slice
my_slice[0] = 999
print("Modified Slice:", my_slice) # Output: [999   4   5]

# Now let's check the original array
print("Original Array after change:", arr1d)
# Output: [  0   1   2 999   4   5   6   7   8   9]
# See! The original array was also modified!


# .copy() method

# This time, let's make a copy
my_copy = arr1d[3:6].copy()

# Now, let's modify the copy
my_copy[0] = 777

print("Modified Copy:", my_copy)      # Output: [777 4 5]
print("Original Array:", arr1d) # The original array is unchanged!