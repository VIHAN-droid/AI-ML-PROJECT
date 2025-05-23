import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('MATPLOTLIB\\batsman_season_record.csv')

batsmen = ["AB de Villiers","DA Warner","MS Dhoni","RG Sharma","V Kohli"]

# plt.bar(df['batsman'],df['2015'],color = "#0AD5F0",width = 0.4)  # will print a bar chart of batsman data in 2015
plt.title("Runs by batsman in 2015")
plt.xlabel("Batsman")
plt.ylabel("Runs")

# now suppose u want to implement multiple bar charts 
plt.bar(np.arange(len(batsmen)) - 0.25 ,df['2015'],color = "#0AD5F0",width = 0.25)
# arange creates numeric sequences
plt.bar(np.arange(len(batsmen)) ,df['2016'],color = "#720AF0",width = 0.25)
plt.bar(np.arange(len(batsmen)) + 0.25 ,df['2017'],color = "#0AF0AB",width = 0.25)

# this way in x axis numbers are marked. To change that use plt.xticks(initial name, final name) fn
plt.xticks(np.arange(len(batsmen)), df['batsman'])

plt.show()



# to print horizontal bar charts  ->  use  plt.barh() 



# PROBLEM -> if the data points on axes have bigger names then they overlap on each other and reduces redability
# in that case use plt.xticks(rotation = 'vertical' )


# STACKED BAR CHART
plt.bar(df['batsman'],df["2015"],label='2015')
plt.bar(df['batsman'],df["2016"],bottom=df["2015"],label='2016')
plt.bar(df['batsman'],df["2017"],bottom=df["2016"]+df["2015"],label='2017')
plt.legend()
plt.show()
