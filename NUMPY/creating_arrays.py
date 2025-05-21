import numpy as np

# creating np arrays from lists

x = range(1,11)
x = list(x)
print(x)

np_arr = np.array(x)
print(np_arr)


# using np.arange(start,stop,step)

np_arr = np.arange(1,10,2)  #[1 3 5 7 9]
print(np_arr)
np_arr = np.arange(1.1,11.9,0.7)
#[ 1.1  1.8  2.5  3.2  3.9  4.6  5.3  6.   6.7  7.4  8.1  8.8  9.5 10.2  10.9 11.6]
print(np_arr)

# for float step values prefer np.linspace(start,stop,num=50,endpoint=t/f,restep= t/f)
        # num -> numbers in the array between start and stop
        # endpoint -> if true then interval = [start,stop] else [start,stop)
        # restep -> if true : returns a tuple = (array,spacing_between_indices)

print(np.linspace(1,10)) 
# [ 1.          1.18367347  1.36734694  1.55102041  1.73469388 ...
print(np.linspace(1,10,5)) 
# [ 1.    3.25  5.5   7.75 10.  ]
print(np.linspace(1,10,5,endpoint=False))  
# [1.  2.8 4.6 6.4 8.2]
print(np.linspace(1,10,5,endpoint=True,retstep=True)) 
#(array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ]), np.float64(2.25))

