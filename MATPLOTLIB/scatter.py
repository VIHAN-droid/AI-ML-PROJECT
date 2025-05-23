import matplotlib.pyplot as plt

# u can use scatter fn to plot

yrs = [2010,2011,2012,2013,2014,2015]
vk = [200,300,305,250,450,520]
plt.title("Runs by VK")
plt.xlabel("Years")
plt.ylabel("Runs by VK")
'''plt.scatter(yrs,vk,color="#1539EFFF")  # same formatting options like plt.plot()
plt.show()'''

# but using plt.plot() is faster for bigger datasets
plt.plot(yrs,vk,"o")  # "o" marks the data points
plt.show()
