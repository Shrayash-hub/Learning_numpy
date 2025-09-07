# Diffrent ways by which we can make arrays using numpy

# 1. Making arrays by using existing data( from list or tuple)
import numpy as np

my_list = [[1, 2, 3], [4, 5, 6]]
arr = np.array(my_list)
print(arr)

# [[1 2 3]
#  [4 5 6]]


# np.asarray(): np.array() jaisa hi hai, lekin agar input pehle se hi ek NumPy array hai, to ye nayi copy nahi banata. Memory bachane ke liye ye accha hai.

# my_list se banayenge to copy banegi
arr_as = np.asarray(my_list)

# arr (jo pehle se numpy array hai) se banayenge to copy nahi banegi
arr_no_copy = np.asarray(arr)


# 2. Arrays with fixed values

# 2.1  np.zeros()
# 2 rows, 3 columns ka array jisme sab 0 ho
zeros_arr = np.zeros((2, 3))
print(zeros_arr)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 2.2  np.ones()
# 4 elements ka 1D array jisme sab 1 ho
ones_arr = np.ones(4)
print(ones_arr)
# [1. 1. 1. 1.]

# 2.3  np.full()
# if we want to fill array with any value
# 3x3 ka array jo 7 se bhara ho
full_arr = np.full((3, 3), 7)
print(full_arr)
# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]

# 2.4  np.zeros_like(), np.ones_like()
# Kisi purane array ka shape aur dtype lekar naya zeros ya ones ka array banate hain.
arr = np.array([[1, 2], [3, 4]])

# arr jaisa hi shape (2,2) ka zeros array
zeros_like_arr = np.zeros_like(arr)
print(zeros_like_arr)
# [[0 0]
#  [0 0]]



# 3. Making it with numerical ranges

# 3.1  np.arange()
# if we want numbers in a sequence  (start, stop, step)
# 2 se shuru, 10 se pehle tak, 2 ke step mein
range_arr = np.arange(2, 10, 2)
print(range_arr)
# [2 4 6 8]


# 3.2  np.linespace()
# 0 aur 10 ke beech 5 equally spaced points
linspace_arr = np.linspace(0, 10, 5)
print(linspace_arr)
# [ 0.   2.5  5.   7.5 10. ]



# 4. Arrays with random data

# 4.1 np.random.rand()
# 0 aur 1 ke beech ke random numbers deta hai (Uniform Distribution).
# 2x3 ka random array
rand_arr = np.random.rand(2, 3)
print(rand_arr)
# [[0.123... 0.456... 0.789...]
#  [0.987... 0.654... 0.321...]]

# 4.2 np.random.randn()
#  Standard Normal Distribution (Gaussian Distribution) se random numbers deta hai, jiska mean 0 aur standard deviation 1 hota hai. Deep learning mein weight initialization ke liye bahut popular hai.

# 2x3 ka random array (normal distribution)
randn_arr = np.random.randn(2, 3)
print(randn_arr)
# [[-0.45...  1.23... -1.89...]
#  [ 0.76... -0.11...  0.34...]]

# 4.3 np.random.randint()
# Ek range ke beech random integers deta hai.
# 1 se 100 ke beech 5 random integers
randint_arr = np.random.randint(1, 100, 5)
print(randint_arr)
# [54 23 87 11 99] (Output har baar alag hoga)



