import pandas
import matplotlib.pyplot as plt
import copy as c
from numpy import *
import numpy as np
import math



def compute_h(price_list,theta_list,training_data,no_of_features,temp,new_array,alpha):
    print(no_of_features)
    for k in range(0,no_of_features+1,1):
       sum=0
       for i in range(0,training_data,1):
           for j in range(0,no_of_features+1,1):
               sum=sum+(theta_list[j]*new_array[i][j])
           sum=(sum-price_list[i])
       temp[k]=temp[k]-(alpha/training_data)*(sum)*(new_array[i][j])
       print(k)



def graph(formula, x_range):
  x = np.array(x_range)
  y = eval(formula)
  plt.plot(x, y, 'b')

f = pandas.read_csv("C:/users/hp/Desktop/data_Set.txt")

[row,col]=np.shape(f)

no_of_features = col - 1

training_data = row

print(training_data,no_of_features)

price_list = list()

theta = list()

#Learning_Rate

alpha = 0.03

#Initial 'b' and 'm' values!

theta.append(-3)

theta.append(4)

x = np.array([f['Population of City in 10,000s'],f['Profit in $10,000s']])

[row_check,col_check]=np.shape(x)

#Transpose the Matrix x
y = x.T

[row1, col1] = np.shape(y)

# We want a column of all the one's

z = np.ones((row1, 1))

# New_Array after adding the ones in one column!

new_array = np.zeros((row1, col + 1))

new_array[:, 0] = z[:, 0]

new_array[:, 1:col + 1] = y


price_list = new_array[:, 2]

for i in range(0,training_data,1):
    temp=list()
    temp=c.copy(theta)
    compute_h(price_list,theta,training_data,no_of_features,temp,new_array,alpha)
    theta=c.copy(temp)
    print(theta[0],theta[1])

graph('theta[0]+theta[1]*x', range(0, 23))

plt.plot(f['Population of City in 10,000s'], f['Profit in $10,000s'], 'ro')

plt.show()
Population of City in 10,000s
