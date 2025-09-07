# Boolean masking is a efficient eay to filter the data, by using an mask (true,false)

import numpy as np

arr = np.array([
    [10, 25, 30],
    [45, 15, 60],
    [70, 85, 90]
])

# Creating the mask
mask = arr < 50

print(mask)

# Apply the mask to the array
print("Filtered Data:\n", arr[mask])
# Output: [60 70 85 90]


## Combining the multiple conditions

# & for AND
# ! for OR

# Condition: Find elements that are greater than 20 AND less than 80
complex_mask = (arr > 20) & (arr < 80)

print("Combined Mask:\n", complex_mask)
# [[False  True  True]
#  [ True False  True]
#  [ True False False]]

print("\nFiltered Data (complex):\n", arr[complex_mask])
# Output: [25 30 45 60 70]


## using mask to modify the data

# Let's change all values greater than 60 to be 0
print("Original Array:\n", arr)

arr[arr > 60] = 0 # Use the mask on the left side of the assignment

print("\nModified Array:\n", arr)
# [[10 25 30]
#  [45 15 60]
#  [ 0  0  0]]