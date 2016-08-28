##########################
###Method and functions ##
##########################
import os
import sys
box = 'C:\Users\chuang\Box Sync\Python\Udemy\\1_PythonBootcamp'
os.chdir(box)
cwd = os.getcwd()
mPath = box + '\Custom_Module'

if not mPath in sys.path: #add modules path to sys path
    sys.path.insert(1,mPath)
del mPath
#####################################################



########
#List Method
########

l=[1,2,3,4,5,6,7]
l.appned(3) #append a 3 to the list
l.count(3) #show frequency
l.extend([4,5,6,7]) #extend the list with a list
l.index(3) #return the index of a value
l.insert(0,'test') #insert an object to a position

#######
#function
#######

def my_func(num1, num2):
    return num1+num2
    
x = my_func(1,2) #return the sum

def is_prime(num):
    """
    INPUT: A number
    OUTPUT: A print statement wheter or not the number is prime
    """
    for n in range(2,num):
        if num%n ==0:
            print 'Not Prime'
            break
    else:
        print 'The number is prime!'

is_prime(12)

#############
#lambda expressions 
#############
square = lambda num: num**2 #one line function using lambda
even = lambda num: num%2==0 # check if it is even
first = lambda s: s[0]
rev = lambda s: s[::-1] #revers string function
adder = lambda x,y: x+y #lambda sum function

print square(10)
print even(3)
print rev('hello')
print adder(10,13)
