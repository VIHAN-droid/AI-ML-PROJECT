import numpy as np

# SCALARS

x = np.array([1,2,3,4,5,6,7,8,9])
print(x)
x += 1
print(x)
x = x / 2
print(x)

# ARITHMETIC OPERATIONS B/W ARRAYS
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.identity(3,dtype=int)
print(x+y) # add corresponding elements of matrices
print(x*y) # multiply corresponding elements of the matrices


# MATRIX MULTIPLICATION
print(np.dot(x,y))  # 2-d : matrix multiplication   &   1-d : inner product

# making arrays as matrices
x = np.asmatrix(x)
print(x)


# BOOLEAN OPERATIONS
a = np.array([[1,2,3],[4,5,6,]])
b = np.array([[1,2,3],[4,2,10]])
print(a==b)
# [[ True  True  True] [ True False False]]

print(np.array_equal(a,b))
# False


# LOGICAL OPERATIONS
a = np.array([[True,True], [False,False]])
b = np.array([[True,False],[False,False]])
print(np.logical_or(a,b))


# BROADCASTING
a = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
b = np.array([1, 2, 3])
print(a+b)
print(a*b) # in both the cases b is treated as [[1,2,3],[1,2,3],[1,2,3]]

# transpose matrix
a = a.transpose()
print(a)
