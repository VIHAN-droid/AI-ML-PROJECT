import numpy as np

dt = np.dtype([('density', np.int32)])
x = np.array([10,20,30], dtype=dt)
print(x)
# this creates a new data type dt and can alse be accessed by print(x['density'])

# MULTIPLE FIELDS

dt = np.dtype([('country','S30'), ('density',np.int32), ('area',np.int32)])
# this creates a data type with country having max 30 chaarcters and density and area with 4 bytes

data = np.array([('India',400,3287), ('USA',36,9834)],dtype=dt)
print(data)
# [(b'India', 400, 3287) (b'USA',  36, 9834)]