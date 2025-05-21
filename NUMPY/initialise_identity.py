import numpy as np

# np.ones((shape) , dtype) if dtype is not specified it takes float values
x = np.ones(7,dtype=int)
y = np.zeros(5,dtype=int)
print(x,y)

x = np.ones((2,6),dtype=int)  # 2-D ones array
print(x)

# empty arrays
x = np.empty(7) # creating an empty array of size 7


# copying arrays
x = np.array([1,2,3,4,5,6,7,8,9])
y = x.copy()
x[0] = 10
print(x)
print(y)


# IDENTITY MATRIX 

# M-1
arr = np.identity(4,dtype=int)
print(arr)
# arr = [[1 0 0 0] [0 1 0 0] [0 0 1 0] [0 0 0 1]]

# M-2
# np.eye(N , M=None , k=0, dtype=float)  -> gives n x m matrix with val at kth diagnol = 1
# k=1 gives upper diagonal and k=-1 gives lower diagonal
x = np.eye(4,4,0,dtype=int)
print(x)
# x = = [[1 0 0 0] [0 1 0 0] [0 0 1 0] [0 0 0 1]]

