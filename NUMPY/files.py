import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])

    # TEXT FILE

# # SAVE FILE  ->  np.savetxt(file, data to be sved, fmt, delimeter=' ', newline, header, footer, comments)
# np.savetxt("file.txt",x,fmt="%1d",delimiter=', ')

# # LOAD FILE  
# x = np.loadtxt("file.txt",delimiter=",")
# print(x)

    # BINARY FILE

# write to a file
# x.tofile(fid, sep="", format="%s")   ->  x: ndarray, fid: file name
y = np.array([[11,22,33],[44,55,66]])
f = open("OOPS\\file.txt","wb")
y.tofile(f)
f.close()

# read file
f = open("OOPS\\file.txt","rb")
print((np.fromfile(f,dtype=int)).reshape(2,3))
f.close()

