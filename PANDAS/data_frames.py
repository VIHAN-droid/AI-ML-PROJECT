import numpy as np
import pandas as pd

# creating dataframes
lst_2d = [[100,80,10], [90,70,7], [120,100,14], [80,50,2]]
# print(pd.DataFrame(lst_2d, columns=['iq','marks','package']))

stud_dict = {'iq':[100,90,120,80], 'marks':[80,70,100,50], 'package':[10,7,14,2]}
# print(pd.DataFrame(stud_dict))

    # CUSTOM INDEXING
stud_dict['name'] = ['A','B','C','D']
stud_data = pd.DataFrame(stud_dict)
stud_data = stud_data.set_index('name')
# print(stud_data)


    # READING DATAFRAMES
movies = pd.read_csv("PANDAS\\movies.csv")
# print(movies)

ipl = pd.read_csv("PANDAS\\ipl-matches.csv")
# print(ipl)



    # ATTRIBUTES AND METHODS

# # shape
# print(movies.shape) # gives  (row,clm)

# # dtype
# print(movies.dtypes) # gives the dtype of all clms

# # index
# print(movies.index)  # RangeIndex(start=0, stop=1629, step=1)

# # columns
# print(movies.columns)

# # values  -> returns a 2-d numpy array containing all the values
# print(movies.values) 

# head and tail
# print(movies.head(3) , '\n' , movies.tail(2))

# # sample() -> gives one random row
# print(movies.sample())

# # info()  -> gives a summary also tells us the non null vals in each col
# print(movies.info()) 

# # describe()
# print(movies.describe())

# # isnull() -> gets the info whether there are missing vals or not in (T/F)
# print(movies.isnull())  # or print(movies.isnull().sum()) for no of nulls in each col

# duplicated()
# print(movies.duplicated())  # or print(movies.duplicated().sum()) for no of duplicates

# rename()
stud_data = stud_data.rename(columns={'package':'lpa'}) # .rename(columns = {old name : new name} )
# print(stud_data)



    # MATH METHODS
# # sum  (same for mean, min, max, median, std, var)
# print(stud_data.sum()) # sums all the values in a clm
# print(stud_data.sum(axis = 1)) # this makes the sum row-wise



    # SELECTING COLS FROM DATAFRAMES
# print(movies['title_x'])   # data type is series
# print(movies[['title_x', 'actors']])  # printing multiple cols


    # SELECTING ROWS FROM DATAFRAMES

# # iloc[]  -> fetches the row from index number
# print(movies.iloc[0])
# print(movies.iloc[0:5])

# # loc[]  -> fetches the row from index label
# print(stud_data.loc['A'])
# print(stud_data.loc['A':'D'])
# print(stud_data.loc[['A', 'C']])


    # SELECTING ROWS AND COLUMNS FROM DATAAFRAMES

# print(movies.iloc[0:3, 0:2]) # gives the 1st 3 rows with 2 clms



    # FILTERING A DATAFRAME  -> ipl data  and  movies data

# Q) find all final winners
new_df = ipl[ipl['MatchNumber'] == 'Final']
# print(new_df[['Season', 'WinningTeam']])

# Q) how many super overs have occured
new_df = ipl[ipl['SuperOver'] == 'Y']
# print(new_df[['Season', 'Date', 'WinningTeam']])
# print(new_df.shape[0]) # how many 

# Q) how many matches has csk won in kolkata
new_df = ipl[ ipl['City'] == 'Kolkata' ]
new_df = new_df[ new_df['WinningTeam'] == 'Chennai Super Kings']
# print(new_df.shape[0])

# Q) toss winner is match winner in percentage
# print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0] / ipl.shape[0] ) * 100 , " %")

# Q) movies with rating higher than 8 and votes > 10000
# print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes']  > 10000)])

# Q) action movies with rating higher than 7.5
# print(movies[ ('Action' in str(movies['genres'])) & (movies['imdb_rating'] > 7.5)].shape[0] 


    # ADDING NEW COLS
movies['country'] = 'India'  # a new col of country is added with val India 

movies['lead_actor'] = movies['actors'].str.split('|').str[0]
# print(movies[['lead_actor','actors']])




    # DATAFRAME FUNCTIONS

# astype -> to change the data type of a clm
ipl['ID'] = ipl['ID'].astype('int32')
# print(ipl.info())

# rest same from series 




# Q) last match played by v kohli in delhi
df1 = ipl[ipl['Team1Players'].str.contains('V Kohli') ]
df2 = ipl[ipl['Team2Players'].str.contains('V Kohli') ]
df = pd.concat([df1, df2])

# print(df[df['City'] == 'Delhi'].head())



# apply()  function

points_df = pd.DataFrame(
    {
        '1st point': [(3, 4), (-6, 5), (0, 0), (-10, 1), (4, 5)],
        '2nd point': [(-3, 4), (0, 0), (2, 2), (10, 10), (1, 1)]
    }
)

def euclidean(row):
    p1 = row['1st point']
    p2 = row['2nd point']
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

points_df['dist'] = points_df.apply(euclidean,axis=1) # axis is 1 since data is used row wise
# print(points_df)
