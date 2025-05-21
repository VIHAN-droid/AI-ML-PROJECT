import numpy as np
# 0 - dim arr
x = np.array(10)
print(np.ndim(x))

# 1-dim arr
x = np.array([10,20,30])
print(np.ndim(x))

# 2-dim arr
x = np.array([[10,20],[30,40]])
print(np.ndim(x))



# SHAPE  (only works for homogeneous arrays)

x = np.array(10)
print(np.shape(x)) 
# ()

x = np.array([10,20,30])
print(np.shape(x))
# (3,)

x = np.array([[10,20,25],[30,40,45]])
print(np.shape(x))
# (2, 3)

# changing the shape of x
x.shape = (1,6)  # product of dimensions should remain same
print(x)