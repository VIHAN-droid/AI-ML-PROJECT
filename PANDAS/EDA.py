import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# getting the data frame
df = pd.read_csv("EDA\\UberDataset.csv")

# getting the columns
clms = df.columns
# print(clms)
# NOTE : numerical -> START_DATE , END_DATE , MILES 
#      : categorical -> CATEGORY
#      : mixed -> START , STOP , PURPOSE

# print(df.head())


# ------------------------------------------------------------------------------------------

    # UNIVARIATE ANALYSIS

# MILES

# print(df['MILES'].describe())
'''
count     1156.000000
mean        21.115398
std        359.299007
min          0.500000
25%          2.900000
50%          6.000000
75%         10.400000
max      12204.700000
'''

# fig, ax = plt.subplots() 
# ax.hist(df[df['MILES'] <= 22]['MILES'].dropna(), bins=25)
# ax.set(title='Dist coverred by Uber Cab drivers',ylabel='Frequency',xlabel='Distance(miles)')
# ax.set_xscale('log')
# ax.set_yscale('log')
# plt.show()

#df[df['MILES'] <=350]['MILES'].plot(kind='box')
# plt.show()

# print(df['MILES'].isnull().sum())

'''
NOTE: CONCLUSION -> 1) DIST ABOVE 22 MILES IS TREATED AS OUTLIER
                    2) MAXIMUM RIDES BOOKED WERE BETWEEN 0-10 MILES (CONSIDERING THE OUTLIERS)
                    3) MAX RIDES BOOKED WERE BETWEEN 0-4 MILES (IGNORING THE OUTLIERS)
                    4) THERE WERE 0 MISSING VALUES

'''



# CATEGORY

# print(df['CATEGORY'].describe())
'''
count         1155
unique           2
top       Business
freq          1078
'''

# print(df['CATEGORY'].isnull().sum())

# plt.pie([1078,1155-1078-1],labels=['Business','Personal'],autopct="%0.1f%%")
# plt.show()


'''
NOTE: CONCLUSION -> 1) RIDES WERE BECAUSE OF EITHER PERSONAL REASONS OR BUSINESS PURPOSES
                    2) 93.3% OF RIDES WERE BECAUSE OF BUSINESS PURPOSES
                    3) THERE WAS 1 MISSING VALUE

'''



# PURPOSE

# print(df['PURPOSE'].describe())
'''
count         653
unique         10
top       Meeting
freq          187
'''

purposes = {}

for j in df['PURPOSE'].dropna():
    if j not in purposes:
        purposes[j] = 1
    else:
        purposes[j] += 1


# plt.pie(purposes.values(),labels=purposes.keys(),autopct='%0.1f%%')
# plt.show()

# print(df['PURPOSE'].isnull().sum() / len(df['PURPOSE']))

'''
NOTE: CONCLUSION -> 1) VALUES WERE SEPARATED BY " / " SO FURTHER ANALYSIS WAS REQUIRED
                    2) MEETING PURPOSES -> 28.6 %
                       MEAL / ENTERTAIN -> 24.5 %
                       ERRAND / SUPPLIES -> 19.6 % MAKING THEM THE MAJOR REASONS FOR BOOKING CABS
                    3) THIS DATA HAD 43.51 % MISSING VALUES

'''
# -------------------------------------------------------------------------------------------------


# MULTI-VARIATE ANALYSIS



# START n END DATE

df['START_DATE'] = pd.to_datetime(df['START_DATE'], errors='coerce')
df['END_DATE'] = pd.to_datetime(df['END_DATE'], errors='coerce')
df['DURATION(MINS)'] = (df['END_DATE'] - df['START_DATE']).dt.total_seconds() / 60


# print(df['DURATION(MINS)'].describe())
'''
count    420.000000
mean      19.326190
std       19.155582
min        0.000000
25%        9.000000
50%       15.000000
75%       22.250000
max      178.000000
'''

# fig, ax = plt.subplots() 
# ax.hist(df[df['DURATION(MINS)'] <= 50]['DURATION(MINS)'].dropna(), bins=25)
# ax.set(title='Duration of travel',ylabel='Frequency',xlabel='Time(mins)')
# ax.set_xscale('log')
# ax.set_yscale('log')
# plt.show()

# df['DURATION(MINS)'].plot(kind='box')
# plt.show()

# print(df['DURATION(MINS)'].isnull().sum() / len(df['DURATION(MINS)']))

'''
NOTE: CONCLUSION -> 1) DURATION ABOVE 50 MINS IS TREATED AS OUTLIER
                    2) MAXIMUM DURATION OF TRAVEL WAS BETWEEN 0-25 MINS (CONSIDERING THE OUTLIERS)
                    3) MAXIMUM DURATION OF TRAVEL WAS BETWEEN 0-20 MINS (IGNORING THE OUTLIERS)
                    4) THERE WERE 63.66 % MISSING VALUES

'''



# START n STOP CITIES

# print(df['START'].describe())
'''
count     1155
unique     177
top       Cary
freq       201
'''

# print(df['STOP'].describe())
'''
count     1155
unique     188
top       Cary
freq       203
'''

df['SAME_CITY_DROP'] = df['START'] == df['STOP']
# print(len(df[df['SAME_CITY_DROP'] == True]) / len(df['SAME_CITY_DROP']))

start_loc = {}

for j in df['START'].dropna():
    if j not in start_loc:
        start_loc[j] = 1
    else:
        start_loc[j] += 1


# plt.pie(start_loc.values(),labels=start_loc.keys(),autopct='%0.1f%%')
# plt.show()

stop_loc = {}

for j in df['STOP'].dropna():
    if j not in stop_loc:
        stop_loc[j] = 1
    else:
        stop_loc[j] += 1


# plt.pie(stop_loc.values(),labels=stop_loc.keys(),autopct='%0.1f%%')
# plt.show()

'''
NOTE: CONCLUSION -> 1) CARY WAS THE MOST POPULOR LOCATION FOR START AND STOP
                    2) 24.91 % OF RIDES HAD START AND STOP IN THE SAME CITY
                    3) MAJOR START LOCATIONS -> CARY : 17.4 %
                                                UNKNOWN : 12.8 %
                                                MORRISVILLE : 7.4 %
                                                WHITEBRIDGE : 5.9 %

                    4) MAJOR STOP LOCATIONS ->  CARY : 17.6 %
                                                UNKNOWN : 12.9 %
                                                MORRISVILLE : 7.3 %
                                                WHITEBRIDGE : 5.6 %

'''


# DIST V/S DURATION

fig, ax = plt.subplots()
ax.plot(df['DURATION(MINS)'] , df['MILES'] , "ob")
ax.set(title='DISTANCE V/S DURATION OF UBER CAB RIDES', xlabel='Time(mins)',ylabel='Distance(miles)')

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

'''
NOTE: CONCLUSION -> 1) MOST OF THE RIDES WERE BOOKED WITHIN THE FOLLOWING RANGE ->
                        TIME = (10,25) mins  AND  DISTANCE = (1,15) miles
                    2) THERE IS A POSITIVE LINEAR RELATION (AS IT SHOULD BE)
                    3) A STRONG CLUSTER IS FROMED BETWEEN 15 MINS TO 25 MINS SUGGESTING THAT
                       MOST RIDES FALL BETWEEN THAT RANGE

'''
