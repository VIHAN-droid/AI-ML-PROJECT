import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

    # SERIES FROM LIST

arr = [1,2,3,4,6,7]
# print(pd.Series(arr))  # prints the arr series and index from 0

# custom index
marks = [81,78,90,72]
subj = ['maths','eng','sci','hindi']
x = pd.Series(marks,index=subj,name="Marks of a student")
# print(x)
"""
maths    81
eng      78
sci      90
hindi    72
Name: Marks of a student, dtype: int64
"""


    # SERIES FROM DICT  -> keys become the indices and values consist the series/1-D array
marks_dict = {}
for i in range(len(marks)):
    marks_dict[subj[i]] = marks[i]
x = pd.Series(marks_dict)
#print(x)  
"""
maths    81
eng      78
sci      90
hindi    72
dtype: int64
"""



    # ATTRIBUTES

# # size
# print(x.size)  #  ->  4
# # dtype
# print(x.dtype) #  ->  int64
# # name
# print(x.name)  #  ->  None (since no name was specified)
# # unique elements or not (if even one element is repeating then it will return False)
# print(x.is_unique)  #  ->  True
# # index
# print(x.index)  #  -> Index(['maths', 'eng', 'sci', 'hindi'], dtype='object')
# # values
# print(x.values)  #  ->  [81 78 90 72]




    # Read CSV 

# single clm

subs = pd.read_csv('PANDAS\\subs.csv') #automatically gives a dataframe file 
# to get a series ->
subs = subs.squeeze()
# print(subs)

# 2 clms

runs = pd.read_csv("PANDAS\\kohli_ipl.csv",index_col='match_no')
runs = runs.squeeze()
#print(runs)

movies = pd.read_csv("PANDAS\\bollywood.csv",index_col='movie')
movies = movies.squeeze()


    # SERIES METHOD

# # head()
# print(subs.head()) # by default it prints top 5 values
# print(subs.head(3)) # to get the top 3 values

# # tail()
# print(subs.tail()) # last 5 rows
# print(subs.tail(2)) 

# # sample()
# print(runs.sample()) # returns any random \value from the sample
# print(runs.sample(3)) # 3 random vals

# # value_counts -> calculates the frequency of data in series and prints the data in descending order
# print(movies.value_counts())  

# # sort_values()  -> sorts the data according to the values
# print(runs.sort_values())
# print(runs.sort_values(ascending=False)) # to print in descending order
# print(runs.sort_values(ascending=False).head(1).values) -> [113]

# # sort_index()  -> sorts the data according to the indices
# print(movies.sort_index())  # and so on ... (similar to sort_values())




    # SERIES MATHS METHODS

# # count()  -> gives the size of series (does not count the missing values unlike size)
# print(runs.count())

# # sum() n product() -> calculates the sum/product of items in the series
# print(subs.sum())

# # mean median mode std var
# print(subs.mean(), subs.median(),'\n', movies.mode(), subs.std(), '\n', subs.var())

# # min() n max()
# print(subs.min())
# print(subs.max())

# # describe()  -> provides the summary of the data
# print(subs.describe())




    # SERIES INDEXING  -> same as lists BUT negative indexing does not work on int index
x = pd.Series([2,3,1,5,6,2,7,8])
# print(f"{x[0]} , {x[2:]} , {x[5::-1]} etc")


    # SERIES EDITING 
marks = [81,78,90,72]
subj = ['maths','eng','sci','hindi']
x = pd.Series(marks,index=subj,name="Marks of a student")

x[1] = 100  # will change the marks of eng from 78 to 100
# print(x)

x['sst'] = 79  # will create a new data in the series
# print(x)

x[[0,2,3]] = [90,90,90]  # editing using fancy indexing
# print(x)



''' 
NOTE : py fns like min max dir sorted len type works on series
     : type conversion works. ex. -> list(x) dict(x) etc
     : using 'in' 'not in' operators in series ( WORKS ONLY ON INDICES ) 
       to use on values do-> 'string' in movies.values
     : loops also works but on values
'''

    # ARITHMETIC OPERATORS
# print(100-x)

    # RELATIONAL OPERATORS
# print(runs >= 50)

    # BOOLEAN INDEXING
# print(runs[runs >= 50])



# PLOTTING USING PANDAS
subs.plot()
# plt.show()
movies.value_counts().head(10).plot(kind="bar")
# plt.show()
