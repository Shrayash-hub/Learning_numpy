# NumPy represents missing numerical data using the special floating-point value np.nan, which stands for "Not a Number".

""" 
np.nan has two important properties you must know:

It's contagious: Any arithmetic operation involving np.nan results in np.nan. (e.g., 5 + np.nan is np.nan).

It never equals itself: Comparing np.nan to anything, including itself, will always be False. This is a common trap for beginners.
"""

import numpy as np

print("5 + np.nan =", 5 + np.nan) # Output: nan
print("Is np.nan == np.nan?", np.nan == np.nan) # Output: False


## Finding Missing Values : np.isnan()

arr = np.array([1, 5, np.nan, 8, np.nan, 12])

# Create a boolean mask to find NaNs
nan_mask = np.isnan(arr)
print("Original Array:", arr)
print("Boolean Mask (is a value NaN?):", nan_mask)
# Output: [False False  True False  True False]


### 2. Replacing Missing Values (Imputation)

# Create a copy to avoid changing the original array
arr_copy = arr.copy()

# Replace all NaN values with 0
arr_copy[np.isnan(arr_copy)] = 0
print("Array with NaNs replaced by 0:", arr_copy)
# Output: [ 1.  5.  0.  8.  0. 12.]


# 1. Calculate the mean of the array, ignoring NaNs
mean_val = np.nanmean(arr)
print("\nMean of non-NaN values:", mean_val) # Output: 6.5

# 2. Fill the NaN values with the calculated mean
arr_copy = arr.copy()
arr_copy[np.isnan(arr_copy)] = mean_val
print("Array with NaNs replaced by the mean:", arr_copy)
# Output: [ 1.   5.   6.5  8.   6.5 12. ]


# 3. using nan_to_num() function 

arr = np.array([1, np.nan, 2, np.inf, 3, np.neginf])
print("Original Array:\n", arr)

# Replace special values with defaults
cleaned_arr = np.nan_to_num(arr)
print("\nCleaned Array (default):\n", cleaned_arr)
# [ 1.00000000e+00  0.00000000e+00  2.00000000e+00  1.79769313e+308
#   3.00000000e+00 -1.79769313e+308]


# syntex : np.nan_to_num(arr, 0, posinf=..,neginf=-..)
