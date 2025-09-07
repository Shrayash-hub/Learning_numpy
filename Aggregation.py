import numpy as np

a = np.array([10,20,30])

# Sum of all the elements of the array
print("Total Sum of a:", a.sum())

# average of all the elements of the array
print("Mean of a:", a.mean())

# minimum of all the elements of the array
print("Min of a:", a.min())

# maximum of all the elements of the array
print("Max of a:", a.max())

# standard deviation of all the elements of the array
print("Standard deviation: ",a.std())

# variance of all the elements of the array
print("Variance: ",a.var())


# we can also use parameters to perform these operation on a particular row or clm

arr = np.array([[2,3,4],
                [5,6,7],
                [8,9,10]])

# addition of each clm
print("Column wise sum:", a.sum(axis=0)) # Output: [4 6] -> [1+3, 2+4]

# addition of each row
print("Row wise sum:", arr.sum(axis=1)) 