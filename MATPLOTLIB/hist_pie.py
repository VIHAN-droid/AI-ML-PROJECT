import matplotlib.pyplot as plt

runs = [33, 78, 12, 1, 56, 89, 43, 21, 67, 38, 50, 91, 5, 73, 60, 18, 102, 40, 36, 28]
# plt.hist(runs) # will create bins on its own
# plt.show()

plt.hist(runs,bins=[10,20,30,40,50,60,70,80,90,100,110])
# plt.show()

# ----------------------------------------

marks = [21,24,23,25,23]
subj = ['eng','maths','hindi','sci','sst']
plt.pie(marks,labels=subj, autopct='%0.1f%%') # autopct -> to print the % contibution on pie chart
#plt.pie()  add colors=[1,2,3,4,5,6] for customizing colors
# plt.show()

# adding plt.pie(explode=[0,0.2,0,0,0,0]) ## that first indexed batsman will appear a bit detached from rest

# plt.style.available to get available styles and plt.style.use(style name) to use that style
