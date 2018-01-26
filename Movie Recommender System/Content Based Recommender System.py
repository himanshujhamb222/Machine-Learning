import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#column headers for the dataset

rating_cols = ['user id','movie id','rating','timestamp']
movie_cols = ['movie id','movie title','release date',
'video release date','IMDb URL','unknown','Action',
'Adventure','Animation','Childrens','Comedy','Crime',
'Documentary','Drama','Fantasy','Film-Noir','Horror',
'Musical','Mystery','Romance ','Sci-Fi','Thriller',
'War' ,'Western']
user_cols = ['user id','age','gender','occupation',
'zip code']

#importing the data files onto dataframes

users = pd.read_csv('C:/Users/hp/Desktop/user.txt', sep='|',
names=user_cols, encoding='latin-1')
movie_details = pd.read_csv('C:/Users/hp/Desktop/movies.txt', sep='|',
names=movie_cols, encoding='latin-1')
ratings = pd.read_csv('C:/Users/hp/Desktop/ratings.txt', sep='\t',
names=rating_cols, encoding='latin-1')



print(ratings)
#Getting the Rating Matrix i.e. Which User has rated which movie

rating_matrix=np.empty((1682,943))
rating_matrix[:] = np.nan

for index in range(0,100000):
    rating_matrix[ratings['movie id'][index]-1][ratings['user id'][index]-1]=ratings['rating'][index]

print(rating_matrix)
[row,col]=np.shape(rating_matrix)
print(row,col)

movie_number=movie_details['movie title']

theta_matrix=np.zeros((19,943))

#Setting Category Rating Matrix

category_dict={1:'Action',2:'Adventure',3:'Animation',4:'Childrens',5:'Comedy',6:'Crime',7:'Documentary',8:'Drama',9:'Fantasy',10:'Film-Noir',11:'Horror',
12:'Musical',13:'Mystery',14:'Romance ',15:'Sci-Fi',16:'Thriller',
17:'War' ,18:'Western'}

category_rating_matrix=np.zeros((1682,19))

for j in range(0,1682):
    category_rating_matrix[j][0]=1

for i in range(0,18):
    category_rating_matrix[:,i+1]=movie_details[category_dict[i+1]]

#print(category_rating_matrix)

#Implementing Gradient Descent!!

alpha=0.01
#
for user in range(0,943):
    for category in range(0,19):
        sum=0
        # j iterates over number of users (943), i iterates over number of movies (1682)
        for j in range(0,943):
            for i in range(0,1682):
                if rating_matrix[i][j]!='nan':
                    sum=sum+((np.matmul(theta_matrix[:,j].transpose(),category_rating_matrix[i,:].transpose()))-rating_matrix[i][j])*category_rating_matrix[i][category]
        theta_matrix[category][user]=theta_matrix[category][user]-alpha*sum


print(theta_matrix)
