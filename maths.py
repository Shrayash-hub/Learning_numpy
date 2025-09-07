import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# ELEMENT WISE ARITHMETIC OPERATION
# we can apply operations on the corresponding elements of the arrays

print("Sum:\n", a + b)

print("Difference:\n", b - a)

print("Product:\n", a * b)

print("Division:\n", a / 2)

# Or we can also direclty apply operations

print(a+100) # going to apply on each element of the array
print(a*10)
print(a/3)


# UNIVERSAL FUNCTIONS

# find the square roots of each element
print("Square Root of a:\n", np.sqrt(a))

# find the  exponential (e^x) of each element
print("Exponential of a:\n", np.exp(a))

# find the sine of each element
print("Sine of a:\n", np.sin(a))