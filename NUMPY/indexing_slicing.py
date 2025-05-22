import numpy as np
# indexing 
x = np.array([1,2,3,4,5,6])
print(x[0],x[-1])

# accessing multi-dim element

    # inefficient method -> it creates and intermediate arr i.e x[1] and then access [0] from it
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[1][0])

    # efficient method 
print(x[1,0])


#slicing

    # 1 - DIM ARR - same as lists
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:]) # [1 2 3 4 5 6 7 8 9]
print(x[:4]) # [0 1 2 3]

    # 2 - DIM ARR 
x = np.array([[11, 12, 13, 14, 15],[21, 22, 23, 24, 25],[31, 32, 33, 34, 35],[41, 42, 43, 44, 45]])
print(x[2:,1:])
# [[32 33 34 35]
#  [42 43 44 45]]


# SLIICING IMP CONCEPT
x = np.array([1,2,3,4,5,6,7,8,9]) 
print(x)
#[1 2 3 4 5 6 7 8 9]
s = x[2:7]
s[0] = 100
s[-1] = 200
print(x)
#[  1   2 100   4   5   6 200   8   9]  
#  if you modify the sliced array it modifies the original one s is not a copy of x

