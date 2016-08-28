#####################################
### use numpy
####################################

########
#Array
########

import numpy as np
my_list1 = [1,2,3,4]
my_list2= [11,22,33,44]
my_lists = [my_list1,my_list2]
my_array = np.array(my_lists)
print my_array                  #create a matrix
print my_array.shape            # 2 by 4 list , demesions
print np.zeros((5,5))           # 5 by 5 zero matrix
print np.ones((5,5))            # 5 by 5 1 matrix
print np.eye((5))               # 5 by 5 identity matix 
print np.arange(5,50,2)         # a vector, from 5 to 50 step 2

### scalars
arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
arr1*arr1           #. multiplication 
arr1-arr1           #. subtraction 
arr1**3             #. power

### array index ####### slice of arrary will affect the original array
tempArr = arr1[0][1:]       # extract value from a matrix 
tempArr2 = arr1[:2,1:]      # 2d array slicing 
tempArr[:] = 100            #change values of the entire array #it will change the original array
tempArr[1:] = 5             #change part of the array   # it will change the original array
copyArr2 = tempArr.copy()   #copy an array, change this will not change the original array 
tempArr = arr1[[1,2]]       # fansy index, return rows as in the input list 

######
#Array transposition 
######
arr = np.arange(50)
arr = arr.reshape((10,5))       #reshae an vecor to a matrix, 10 by 5
print arr
print arr.T                     #transpose an array 
print np.dot(arr.T, arr)        #dot multiplication 

###some array functions 
arr = np.arange(50)
np.sqrt(arr)              #square root of all elements 
np.exp(arr)               #e to the power of all array elements
A = np.random.randn(10)         #random 10 values from normal distribution 
B = np.random.randn(10)
np.add(A,B)                 #add two array 
print np.maximum(A,B)       # . pick the bigger element of two array 
#look up more array functions
website = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'
