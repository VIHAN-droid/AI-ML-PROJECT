# import matplotlib.pyplot as plt

# plt.plot([-5,7,12,25]) # plots a continous curve
# # plt.show()
# plt.plot([-5,7,12,25],"ob")  # plots a discrete curve
# # plt.show()

# # formatting
# days = range(1,9)
# celsius_val = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

# fig, ax = plt.subplots()
# ax.plot(days,celsius_val)  # ax for axes 
# ax.set(xlabel = 'Day', ylabel = 'Temp(C)', title = 'Temp Graph')  # sets the axes' names
# # plt.show()

# # MULTIPLE PLOTS
# days = list(range(1,9))
# celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
# celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
# fig, ax = plt.subplots()
# ax.set(xlabel = 'Day', ylabel = 'Temp(C)', title = 'Temp Graph')

# ax.plot(days,celsius_min,days,celsius_min,"ob",days,celsius_max,days,celsius_max,"or")
# plt.show()

# # above plot works as -> ob : circle marks at (x,y) of blue color


# ''' format string chars:
# -b : solid blue
# --b : dotted blue
# -.b : dash-dot blue   ,etc
# '''

# # CHANGING THE LIMITS OF AXES

# print(ax.axis())  # current limits of axes

# days = range(1,9)
# celsius_val = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

# ax.axis([0,10,0,50])
# ax.plot(days,celsius_val)
# plt.show()



# ------------------------------------------------------------------------------


import matplotlib.pyplot as plt

yrs = [2010,2011,2012,2013,2014,2015]
vk = [200,300,305,250,450,520]
rs = [400,200,300,350,400,310]

# plt.plot(yrs,vk,yrs,rs)
plt.title("Career comparison b/w vk and rs")
plt.xlabel("Year")
plt.ylabel("Runs Scored")

# plt.show()

# To change the color of the graphs

# plt.plot(yrs,vk,color= "#69f111")
# plt.plot(yrs,rs,color="#0867f9")
# plt.show()

# formatting

#  plt.plot(yrs,vk,color="#69f111",linestyle=":", linewidth=3) # for a dotted line and change the width


# moreformatting options
# plt.plot(yrs,rs,marker='+',markersize=10)  # marker ((x,y) points) can be + . < etc

# note that instead of using markers u can do ->
# plt.grid()

# plt.show()


# LABELLING OF LINES 

# plt.plot(yrs,vk,color= "#69f111",linestyle='--',label='Virat Kohli')
# plt.plot(yrs,rs,color="#0867f9",linestyle='--',label='Rohit Sharma')
# plt.legend()  # call this function to get the labels marked
# plt.show()



# IMP EXAMPLE
'''
SUPPOSE U R GIVEN WITH A LIST OF VIEWS ON UR YT VIDEOS THAT U UPLOAD DAILY AND SUDDENLY AFTER DAY 7
THE VIEWS SHOOT UP. IN THAT CASE IF U PLOT A LINE GRAPH THE VARIATION WON'T BE MUCH IN COMPARISON
TO THE HUGE AMT OF VIEWS U GOT ON THAT DAY AND MATPLOT CURVE WILL BE FLAT
IN THAT CASE U SET LIMITS ON  AXES
'''
# LIMITING AXES

# views = [100,250,125,167,250,220,100000]
# days = [f"Day {i}" for i in range(1,8)]
# plt.title("Views on Yt")
# plt.plot(days,views,color="#07EF9E",label="views")
# plt.legend()
# plt.xlabel("Days")
# plt.ylabel("Views")
# # SETTING THE LIMITS
# plt.xlim("Day 1","Day 3") # to chech variations from day 1 to day 3
# plt.ylim(0,1000) # to check variation over views from 0 to 1K
# plt.show()
