"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

#Importing functions I will later use in the program
from math import sqrt
import numpy as np

#Solving part A, a., using only for-loops
i = 1

def std_loops(x):
    sum1 = 0
    sum2 = 0
#Using a for loop to sum the elements of the sequence
    for i in range(1, x+1):
        sum1 = sum1 + i
        mean = sum1 / x

#In the same loop, adding together the squares of the sequence
        sum2 = sum2 + i ** 2
        S = sum2 / x
        
#Raising i by one each time the loop runs
        i = i + 1

    # Computing the variance
    var = S - mean ** 2

    # Computing the standard deviation
    std = sqrt(var)

    return std

print(f'The standard deviation using for-loops is: {std_loops(5)}')

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """


#Solving part A, b. , using built-in functions

def std_builtin(x):
#Using built-in functions of Python to compute the variables
    num_lst=[int(1),int(2),int(3),int(4),int(5)]
    squared_lst=(num **2 for num in num_lst)
    
    
    mean2=sum(num_lst)/x
    
    S2=sum(squared_lst)/x
    
    var2=S2-mean2**2
    
    std2=sqrt(var2)
    
    return std2

print(f'The standard deviation using built-in functions is: {std_builtin(5)}')



#part A, c. using python's proper function for finding the standard deviation

num_lst=[int(1),int(2),int(3),int(4),int(5)]
std3=np.std(num_lst)

print(f'The standard deviation using NumPy is:  {std3}')
    
