import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
print(x == 4) # [False False False  True False False False False]
# can do same for n dimensional array

# FANCY INDEXING
y = np.array([9,8,7,6,5,4,3,2,1])  # size should be same 
print(x[y<=2])  # matches the index in bot x and y (ex: y=2 satisfies and index = 7 so x[7] is printed)
# [8 9]


# PRINTING MULTIPLE INDICES
print(x[[0,2,4,5]])  # [1 3 5 6]

# example
even_x = x[x%2 == 0]
print(even_x) # [2 4 6 8]



# MATRIX

x = np.array([1,2,3])
y = np.array([1,5,8])

# dot product
print(np.dot(x,y))

# cross product
print(np.cross(x,y))

