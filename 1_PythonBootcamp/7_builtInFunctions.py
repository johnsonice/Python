#####################################
#### Built in functions #############
#### And Decorators #################
#####################################

############
## function map()
############

#example 1
temp =[0,1,22,40,100]
print map(lambda T: (9.0/5)*T + 32, temp) #lika array operation, apply the formula to all element in the list

#example 2
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print map(lambda x,y,z: x+y+z, a,b,c) #array sum, this is . operation, not matrix operation

############
## function reduce()
############

#example 1 
lst = [1,2,3,555,6888,99997766]
max_find = lambda a,b: a if (a>b) else b #compare two values
print reduce(max_find,lst) #find the max in a list 

############
## function filter()
############

#example 1 
lst = [1,2,3,555,6888,99997766]
def even_check(num):
    if num%2==0:
        return True
    else:
        return False

print even_check(35)
print filter(even_check,lst) #filter out all true values 
print filter(lambda num: num%2==0, lst)
print filter(lambda num: num>3, lst) #values greater than 3

############
## function zip()
############

#example 1 
a = [1,2,3]
b = [4,5,6,7,8,9]

print zip(a,b) # return [(1,4),(2,5),(3,6)]
for pair in zip(a,b):
    print max(pair) #print out the bigger in two list
print map(lambda pair: max(pair), zip(a,b)) #put bigger one into a list

#example 2
#zip a dictionary
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
def switcharoo(d1,d2):
    dout = {}
    for d1key, d2val in zip(d1,d2.itervalues()):
        dout[d1key] = d2val 
    return dout
print switcharoo(d1,d2)

############
## function enumerate()
############

#example 1 
l = ['a','b','c','fasd',True]
for (count,item) in enumerate(l): #it will keep a count variable 
     #count start from 0
    if count >2:
        break
    else:
        print item
        
############
## function all() any()
############

l=[True,True,False,False]
print all(l) #will return False, because not all element are true
print any(l) # will return True, because some are tures

#############
##Decorators 
#############
s = 'This is a global variable'

def func():
    s2 = 'this is a local variable'
    print locals() #print local variables 
print globals() #print all global variables
#can assing a variable to a function
pl = func
pl()

#############
## Functions within Functions 
#############

def hello(name):
    print 'Hello ' + name
    def greet():
        return '\t This is inside the greet() function'
    def welcome():
        return '\t This is inside the welcome() function'

    if name =='Chengyu':
        return greet
    else:
        return welcome
    
x = hello(name='Chengyu') #x is a retuned function 
print x() 

#############
## Functions as argument
#############

def hello(name):
    print 'Hello ' + name
def other(func,name):
    print 'Other code goes here!'
    print func(name)
other(hello,name='Chengyu')

