import numpy as np

# FLATTEN   a.flatten()  or  a.ravel()
a = np.array([[[ 0, 1],[ 2, 3],[ 4, 5],[ 6, 7]],[[ 8, 9],[10, 11],[12, 13],[14, 15]]])
print(a)
print(a.flatten())
lst = [int(z) for x in a for y in x for z in y]
print(lst)

# a.flatten() and lst gives same output


# RESHAPE ARRAY  a.reshape(shape)
x = np.arange(1,9)
print(x.reshape(2,2,2))
# [[[1 2]  [3 4]] [[5 6]  [7 8]]]

# CONCATENATE arr
x = np.concatenate(([1,2,3,4],[5,6,7],[8,9]))
print(x)

# concatenate((arrays), axis) if axis = 1 then they are joined along columns (if they hv same no of rows)


# ADDING NEW DIMENSIONS
x = np.array([2,5,18,14,4]) 
y = x[:, np.newaxis]  # new dimension is added 
print(y)

# VECTOR STACKING
A = np.array([3, 4, 5])
B = np.array([1,9,0])
print(np.vstack((A, B)))  # row_stack
print(np.column_stack((A, B))) # clm stack


# TILING 
x = np.array([[1,2],[3,4]])
print(np.tile(x, (1,2))) # so matrix will be rep 1 time in x and 2 times in y
# [[1 2 1 2] [3 4 3 4]]

#  for an array 'A' of shape (2, 3, 4, 5), a 'reps' of (2, 2) is treated as (1, 1, 2, 2).



