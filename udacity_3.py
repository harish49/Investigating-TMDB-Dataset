'''
PROJECT : INVESTIGATING A DATASET OF TMDb Data set
'''
'''
SOME DETAILS ABOUT PROKECT :
->The following project is about Investing a data set of TMDb-MOVIES
->The findings and all other parts of project except the CODE , are included in a PDF.
->The code below calculates the results of the findings of the tmdb dataset.
'''
'''
MODULES USED :
->NumPy
->Matplotlib
->Pandas
'''
''' Importing necessary packages'''
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
df=pd.read_csv('tmdb-movies.csv')

''' A VIEW ON TMDb DATA'''
df=pd.DataFrame(df)
df.head()

'''PROPERTIES OF TMDb DATA'''
df.info()

'''DESCRIPTION ABOUT THE IRRELEVANT COLUMNS'''

'''
->id : id is not much useful to provide important information
->imdb_id : Though it is imdb id , it does not play an important role in calculating the statistics
->budget_adj : Not so useful
->revenue_adj : Not so useful
->homepage : It is just a website URL which contains simple movie description which is not helpful in statistics
->Production companies : Though it is one of the factor for the Cast , it is not important for statistics
->Vote average : Not much useful
->taglines : Not much useful
'''
'''REMOVING IRRELEVANT COLUMNS THAT ARE MENTIONED ABOVE'''
df=pd.read_csv('tmdb-movies.csv')
df= df.drop([ 'id', 'imdb_id', 'budget_adj','tagline','revenue_adj', 'homepage','production_companies', 'vote_average'],1)#deleting the columns
df.info()

'''Changing the date format '''
df['releasedate']=pd.to_datetime(df['release_date'])#Using to_date funtion , i changed the format of the data and deleted previous format
df=df.drop(['release_date'],1)
df.head()

'''PROPERTIES OF TMDb DATA AFTER DROPPING IRRELEVANT COLUMNS'''
df.info()

'''Checking and Removing the duplicate rows'''
a=df.shape[0]
df=df.drop_duplicates()#dropping the dupicates and again reassiging after filtering
b=df.shape[0]
print("Number of columns before removing duplicates is ",a)
print("Number of columns after removing duplicates is ",b)

'''Getting rid of zeros and nulls'''
''' 
prints the rows if budget value==0 or revenue value==0  or runtime==0
i am removing  these values  since these entries are not entered 
and mean nothing and are unfit for computation
'''
df[(df['revenue']==0) | (df['budget']==0) |(df['runtime']==0)]

'''REMOVING NAN AND ZERO VALUES '''
df = df[df.budget !=0]# using  boolean technique ,respective rows which has budget column value zero is removed
df=df[df.revenue !=0]# using  boolean technique ,respective rows which has revenue column value zero is removed
df=df[df.runtime!=0]
df.dropna()#removing  null values if any
print("The shape is ")
print(df.shape)#Updated rows and columns

'''Calculating the findings'''

'''
Statistical findings:
->Movie with highest profit ,its budget and revenue
->Movie with lowest profit , its budget and revenue
->Details of most profit gained movie and most loss gained movie
->Movie with most  and least running time
->Number  of movies released before year 2000 and number of movies released after year 2000
->Highest votes count , Least votes count , Average votes count and the movie name
'''

'''
Finding representing with Plots:
->Running time of all movies
->Distribution of Genres
->Top 10 Movies with more votes
->Top 10 Movies with most profits
->Number of Movie releases per an year
->Revenue V/S budget
->Revenue V/S popularity
->Revenue V/S votes
->Revenue V/S profits
'''

'''Movie with highest profit , its budget and revenue'''
df['profit']=df['revenue']-df['budget']#mainating a seperate column called profits of every movie
high_profit_movie=df.loc[df['profit'].idxmax()]['original_title']#using loc to get name wise accessing of data and idxmax to get movie with maximum profits
high_profit_revenue=df.loc[df['profit'].idxmax()]['revenue']#using loc to get name wise accessing of the data and idxmax to get the movie with maximum revenue
high_profit_budget=df.loc[df['profit'].idxmax()]['budget']#using loc to get name wise accessing of the data and idxmax to get the movie with maximum budget
high_profit=df.loc[df['profit'].idxmax()]['profit']
print("The movie with highest profit is ",high_profit_movie)
print("The profit is : ",high_profit)
print("The budget is : ",high_profit_budget)
print("The revenue is : ",high_profit_revenue)

'''Movie with least profit , its budget and revenue'''
least_profit=df.loc[df['profit'].idxmin()]['profit']
least_profit_movie=df.loc[df['profit'].idxmin()]['original_title']#using loc to get name wise accessing of data and idxmax to get movie with minimum profits
least_profit_revenue=df.loc[df['profit'].idxmin()]['revenue']#using loc to get name wise accessing of the data and idxmax to get the movie with minimum revenue
least_profit_budget=df.loc[df['profit'].idxmin()]['budget']#using loc to get name wise accessing of the data and idxmax to get the movie with minimum budget
print("The movie with least profit is ",least_profit_movie)
print("The profit is ",least_profit)
print("The budget is : ",least_profit_budget)
print("The revenue is : ",least_profit_revenue)

'''The details of the most profit movie'''
high_profit_details=pd.DataFrame(df.loc[df['profit'].idxmax()])#printing the details of the movie which has highest profit
display(high_profit_details) 

'''The details of the least profit movie'''
least_profit_details=pd.DataFrame(df.loc[df['profit'].idxmin()])#printing the details of the movie whose profits is least
display(least_profit_details)

'''Movie's running time'''
print("Highest Running time movie : ",df.loc[df['runtime'].idxmax()]['original_title'])#Using loc to calculating highest runtime movie
print("Less Running time movie : ",df.loc[df['runtime'].idxmin()]['original_title'])#Calculating the name of movie

'''Movies released before 2000 and movies released after 2000'''
x=df.loc[df['release_year']>=2000].shape[0]#Using boolean expressions finding number of movies released after the year 2000
y=df.loc[df['release_year']<2000].shape[0]#Using boolean expressions finding number of movies released before the year 2000
print("Number of movies released after year 2000 is ",x)
print("Number of movies released before year 2000 is ",y)

'''Votes statistics'''
print("Highest Votes : ",df['vote_count'].max())#Caclulating the most votes
print("Movie : ",df.loc[df['vote_count'].idxmax()]['original_title'])#Calculating the movie with most votes
print("Lowest Votes : ",df['vote_count'].min())#Calculating the least votes
print("Movie : ",df.loc[df['vote_count'].idxmin()]['original_title'])#Calculating the movie which has least votes

'''Running time of All movies representing with a histogram'''

plt.figure(figsize=(10,6))#Setting the figure size
plt.xlabel('Runtime')#Labelling the x variable
plt.ylabel('Number of Movies')
plt.hist(df['runtime'],rwidth=0.8,bins=30,color = "black", ec="black")#ec is for border to look it moret thicker and setting bin size 30
plt.show()

plt.figure(figsize=(18,18))#Setting the figure size
 
'''
The following operation is for calculating the most popular Genre.
The details of the Genre are not given seperately.They have been clubbed into one another in the genre column
For calculating the statistics ,we have to seperate the generes from one another.
These Genres are seperate by the '|'.
So i am seperating the strings that are delimited by '|'
and the mainting the the Genre names expliicitly in a pandas dataseries 
plotting the pie chart for the above filtered data and setting up the font size 
'''
x=pd.Series(df['genres'].str.cat(sep = '|').split('|'))
x=x.value_counts()
x.plot.pie( 
       autopct='%2.2f%%', textprops={'fontsize': 20})
plt.axis('equal')
plt.tight_layout()
plt.show()
'''Movies V/S votes which plots the top 10 movies '''
dx= pd.DataFrame(df['vote_count'].sort_values(ascending = False))#Sorting the vote count column in descending order
dx['original_title']=df['original_title']#Copying all the movie names of the original dataframe to temporary data frame
movie_names= list(map(str,(dx['original_title'])))#map is used to seperate the names . str determines the type of data and
#copying the filtered data into the movie_names 
x=list(movie_names[:10])#Using slicing technique , taking the first 10 values  and converting them into the list
y=list(dx['vote_count'][:10])#Same as above ,using the slicing technique and taking the top 10 values which are top 10 maximum values
view= sns.pointplot(x=y,y=x)#Setting up the plot
view.set_title("Top 10 Movies with most votes",fontsize = 15) # Setting the title 
view.set_xlabel("Number of votes",fontsize = 13)

'''Top 10 Most profit gained movies'''
dx1= pd.DataFrame(df['profit'].sort_values(ascending = False))#Sorting the vote count column in descending order
dx1['original_title']=df['original_title']#Copying all the movie names of the original dataframe to temporary data frame
movie_names1= list(map(str,(dx1['original_title'])))#map is used to seperate the names . str determines the type of data and
#copying the filtered data into the movie_names 
x=list(movie_names1[:10])#Using slicing technique , taking the first 10 values  and converting them into the list
y=list(dx1['profit'][:10])#Same as above ,using the slicing technique and taking the top 10 values which are top 10 maximum values
view= sns.pointplot(x=y,y=x)#Setting up the plot
view.set_title("Top 10 Movies with most profits",fontsize = 15) # Setting the title 
view.set_xlabel("Profit amount",fontsize = 13)

'''Number of movies released in years'''
dx2=df.release_year.value_counts().sort_index()#Sorting the indexes for better visulisation
dx2.plot(x='year',kind='bar',fontsize = 11,figsize=(20,10))#Setting up the size
plt.title('Years vs Number Of Movie Releases',fontsize = 15)#Giving a title for the histogram
plt.xlabel('Year',fontsize = 13)#Setting up X label
plt.ylabel('Number of movie releases',fontsize = 13)
sns.set_style("darkgrid")#Setting the background style

print(sns.jointplot("revenue", "budget", data=df,kind="reg")) # Plotting a seaborn joint plot in a regession model fashion

print(sns.jointplot("revenue", "popularity", data=df,kind="reg"))#Plotting a seaborn joint plot in regression model fashion

print(sns.jointplot("revenue", "vote_count", data=df,kind="reg"))#Plotting a seaborn joint plot in regression model fashion

print(sns.jointplot("revenue", "profit", data=df,kind="reg"))#Plotting a seaborn joint plot in regression model fashion
