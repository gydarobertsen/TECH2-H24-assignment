
#TECH2 mandatory assignment - Part A


#Importing functions needed in the program
from math import sqrt
import numpy as np

#Solving part A, a., using only for-loops

#Creating a function to compute the standard deviation using for-loops
def std_loops(x):
    sum1 = 0
    sum2 = 0
#Using a for loop to sum the elements of the sequence, setting the limit to the length of the list
    for i in range(x):
        sum1 = sum1 + i

#In the same loop, adding together the squares of the sequence
        sum2 = sum2 + i ** 2
    
#Calculating the mean of the sum of the list, and of the sum of the squared list
    mean = sum1 / x
    S = sum2 / x
#Computing the variance
    var = S - mean ** 2

#Computing the standard deviation
    std = sqrt(var)

    return std

print(f'The standard deviation using for-loops is: {std_loops(5)}')



#Solving part A, b. , using built-in functions

#Creating a function to compute the standard deviation using built-in function
def std_builtin(x):
#Defining the list
    num_lst=[int(1),int(2),int(3),int(4),int(5)]
#Defining the list of the squared elements
    squared_lst=(num **2 for num in num_lst)
    
#Calculating the mean, by summing the lists and dividing by the length
    mean2=sum(num_lst)/x
    S2=sum(squared_lst)/x
    
#Computing the variance
    var2=S2-mean2**2
#Computing the standard deviation
    std2=sqrt(var2)
    
    return std2

print(f'The standard deviation using built-in functions is: {std_builtin(5)}')



#part A, c. using python's proper function for finding the standard deviation

#Creating the list
num_lst=[int(1),int(2),int(3),int(4),int(5)]
#Computing the standard deviation by using NumPy's proper function
std3=np.std(num_lst)

print(f'The standard deviation using NumPy is:  {std3}')
    
