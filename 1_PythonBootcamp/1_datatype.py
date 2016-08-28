#################
###Lecture One###
#################

######working dirctory

import os
cwd = os.getcwd()
box = 'C:\Users\chuang\Box Sync\Python\Udemy'
os.chdir(box)
cwd = os.getcwd()

############################################


#######
#basic numbers 
#######
print 3/2 #if in python 2 you get 1, in python 3, you get 1.5 
print 3.0/2 #use floating number to get 1.5 
print float(3)/2 #will make 3 as float  
print 2**3 #powers 
print 4**0.5 #roots

bin(111) #convert to binary 
pow(2,4,3) # = 2**4 % 3
abs(-2) #return 2
round(3.1415926,2) #return 3.14, round to 2 decimal points



######
#assign variables
######
a = 5  #assign as 5
a = a + a # a will be 10
a += 5 # = a = a + 5 


#######
#string 
#######
print 'This is a string'
print ("I'm also a string") # in python 3, use print()
print '"This is a quote"'
print 'Here is a new line \nand here is the second line' #\n new line 
print 'Here is a new line \tand here is a tab' #\t tab 
#####string functions
s = 'Hello World'
len(s)                  #get the length of the string
s[0]                    #slice out the first letter 
s[1:]                   #slice out from 2 to the end 
s[:-1]                  #get everything but the last letter 
s[::2]                  #get everything step 2 
s[::-1]                 #step -1, = reverse string
s + ', concatenate me.' #use + to concatenate 
s.upper()
s.lower()
s.split(' ')            #split it by space, will return ['Hello','World']
s.partition(' ')        #it will return the seperator as well ['Hello', ' ' ,'World']
s*10                    #duplicate letter for 10 times
s.capitalize()          #capitalize the first letter
s.count('0')            #count the number of o
s.find('o')             #find the first position of o
s.center(20,'-')        #return "-----hello world-----"
s.isalnum()             #is alpha or numeric
s.isalpha()             #is alpha
s.islower()             #any lower case
s.isspace()             #Check if it contains only space
s.istitle()             #check if it is title like "Hello World"
s.endswith('d')         #check if end with 'd'


#######
#print formatting
#######
x = 'String'
print 'Place my variable here: %s' %(x) #place a variable value in a string
print 'First: %s, Second: %s, Thir: %s' %('Hello','two',3)
print 'First: {x} Second: {y} Third{x}'.format(x='inserted',y='two') # use print format
print 'Floating pint number : %1.2f' %(12.1415926) #show at least 1 integer number and 2 decimals 


#######
#list
#######

my_list = [1,'hello','world',4,5,19] #list can hold any type of data
len(my_list)
my_list[0] #the first element 
my_list[1:] #the same as string slicing etc 
my_list = my_list + ['new','item',11,12,13] #append a list to a list 
my_list*2 #duplicate the elements in the list 

##list function 
l = [1,2,3,4]
l.append(['append me',5])
l.extend([1,44,5,4])        #add all the element in the list to the original list          
l.pop()                     #extract the last element of the list 
l.pop(0)                    #extract the first element of the list, the original list will no have [0]
l.index(44)                 #get the index of a value
l.insert(0,'inserted')      #place 1111 in position 0 
l.remove('inserted')        #remove the first instance of the element

##list sort 
l=['a','b','c','d']
l.reverse()                 #reverse the order of the list 
l.sort()                    #sort the list

##nested list 
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = [l_1,l_2,l_3]
matrix[1][1] # this will return 5 
first_col = [row[0] for row in matrix] # get the first column of he matrix [1,4,7]


#######
#dictionary 
#######
my_dict={
    'k1':'first value',
    'k2':2,
    'k3':'string'
         }
my_dict['k1'] #get value from dictionary
my_dict['k1'].upper() #chain other method 
#create dictionary and then assing keys and value
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
#nested dictionary
d = {
    'k1':{
        'kk1':123
        },
    'k2':{
        'kk2':223
        }
    }
d['k1']['kk1']

#dictionary compression 
d = {x:x**2 for x in range(10)} #return {0:0,1:1 .......}
d = {k:v**2 for k,v in zip(['a','b'],range(2))} #return {a:0,b:1........}

for k,v in d.items(): #or use d.iterkeys, d.iteritems, d.itervalues
    print 'someting'
#dictionary properties
d.keys()        #get all keys
d.values()      #get all values
d.items()       #convert dictionary to a Tuple
d.viewvalues()  #look at the values of the dictionary 

#######
#Tuples  
#######
t = ('one',2,2,3)
len(t)
t.index(3) #return the position of 2 in the tuple
t.count(2) #frequency of 2
#############tuples is inmmutable

#######
#####Files 
#######
f = open('test.txt')
f.read() #read the file 
f.seek(0) #return the cursor back to begaining 
f.readlines()#read each line, put it in to a list
f.seek(0)
#print each line of the text file
for line in f:
    print line

#######
#####Set and Booleans
#######
    #set only contain unique values 
x = set()
x.add(1)
x.add(2)
x.add('string')
l =[1,1,1,1,2,2,2,3,3,3]
x=set(l)                    #x = {1,2,3}
x.discard(1)                #drop one element
list(x)[0]                  #convert set to list and extract values

s1={1,2,3}
s2={1,2,4}
s3={5}
s1.intersection(s2)         #return {1,2}
s1.intersection_update(s2)  #make s1 = {1,2}
s1.isdisjoint(s2)           #check if don't have intersections, here will return false
s1.issubset(s3)             #check if is subset of another set
s2.issuperset(s1)           #check if is superset
s1.symmetric_difference(s2) #get the symmetric difference
s1.union(s2)                #combine two sets 
s1.update(s2)               #combine the two sets and update hthe 


a = True #Booleans 
b = None #none value
x = 1<2 and 2<3 #return true
x = 1<2 or 2>3 #return true












