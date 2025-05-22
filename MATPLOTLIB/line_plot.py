import matplotlib.pyplot as plt

plt.plot([-5,7,12,25]) # plots a continous curve
# plt.show()
plt.plot([-5,7,12,25],"ob")  # plots a discrete curve
# plt.show()

# formatting
days = range(1,9)
celsius_val = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

fig, ax = plt.subplots()
ax.plot(days,celsius_val)  # ax for axes 
ax.set(xlabel = 'Day', ylabel = 'Temp(C)', title = 'Temp Graph')  # sets the axes' names
# plt.show()

# MULTIPLE PLOTS
days = list(range(1,9))
celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
fig, ax = plt.subplots()
ax.set(xlabel = 'Day', ylabel = 'Temp(C)', title = 'Temp Graph')

ax.plot(days,celsius_min,days,celsius_min,"ob",days,celsius_max,days,celsius_max,"or")
plt.show()

# above plot works as -> ob : circle marks at (x,y) of blue color


''' format string chars:
-b : solid blue
--b : dotted blue
-.b : dash-dot blue   ,etc
'''

# CHANGING THE LIMITS OF AXES

print(ax.axis())  # current limits of axes

days = range(1,9)
celsius_val = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

ax.axis([0,10,0,50])
ax.plot(days,celsius_val)
plt.show()
