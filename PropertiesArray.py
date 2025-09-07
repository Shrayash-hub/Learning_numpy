import numpy as np

arr = np.arange(1,10).reshape(3,3)

# 1. arr.ndim() : its going us to tell the dimensions of the array
print(arr.ndim)
# Output : 2 ( two dimensional )

# 2. arr.shape() : its going to return an tuple , telling about the size of array in every dimension

print(arr.shape)
# Output: (3, 3)  (Matlab 3 rows aur 3 columns)
# we can get count of total elements by multiplying the numbers of shape

# 3. arr.size() : give the count of total elements in the array

print(arr.size)
# Output: 9


#  ARRIBUTES RELATED TO MEMORY AND DATATYPE

# 1. arr.dtype(): gives the datatype of the element present in the array

print(arr.dtype)
# Output: int64 (Platform ke hisab se int32 bhi ho sakta hai)

# 2. arr.itemsize(): it tells about the size of memory occupied by the each element of the array

print(arr.itemsize)
# Output: 8 (Kyunki ek int64 element 8 bytes leta hai)

# 3. arr.nbytes(): its going to tell us how much memory is accupied by the whole array   ( arr.size()*arr.itemsize() )
print(arr.nbytes)
# Output: 72 (Kyunki 9 elements * 8 bytes = 72)

# 4. arr.astype(required_type): its going to covert the datatype of the each element in the array
arr_int = arr.astype(float)
print(arr_int)


# ATRRIBUTES RELATED TO DATA MANIPULATION

# 1. arr.T() : it return the transpose view of the array, without changing the original array

print(arr.T)
# Output:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

# 2. arr.real() and arr.imag() : if there are any complex number in our array then .real is going to return the real part and .imag is going to return the imaginary part

complex_arr = np.array([1+2j, 3+4j])

print(complex_arr.real) # Output: [1. 3.]
print(complex_arr.imag) # Output: [2. 4.]


