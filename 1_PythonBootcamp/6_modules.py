############################################
####  Modules ##############################
############################################


############
## module inport custom module imports
############

import os
import sys
box = 'C:\Users\chuang\Box Sync\Python\Udemy\\1_PythonBootcamp'
os.chdir(box)
cwd = os.getcwd()
mPath = box + '\Custom_Module'

if not mPath in sys.path: #add modules path to sys path
    sys.path.insert(1,mPath)
del mPath

import hello 
hello.helloworld()


######################
##Collection module 
######################

########counter#######
from collections import Counter
#example 1
l = [1,1,1,1,2,2,2,2,34,45,5,2,2345,234,26]
x = Counter(l)
print x[1]

#example 2
s = 'How many times does each word show up in this sentence. word word show up up. it is good. I like this. I dont like this.'
words = s.split()
c = Counter(words)
common = c.most_common(2) #show 2 most common word
print 'most common word is "%s". it shows up %s times.' %(common[0][0], common[0][1])
#other properties
print sum(c.values())   # total of all counts
list(c)                 # convert to unique elemetns
set(c)                  # convert to a set
dict(c)                 # convert to a dictionary
c.items()               # convert to a list of (elem,cnt) pairs
c.most_common()[:-n-1:-1] # n least common elements
c += Counter()          # remove zero and negative counts
c.clear()               #reset all counts


########defaultdict#######
from collections import defaultdict
d = defaultdict(lambda: None)
d['one'] #it won't throw an error, it will default to none
d['two'] = 2
print d

######### ordered dictionary ###############
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
for k,v in d.items(): 
    print k,v #it will retain the order of how the dictionary is populated 

######### namedtuple ###############
from collections import namedtuple
#it almost like a class object, has named field with it 
Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab', name='sam')
print sam.age #but attribute can not be changd 


######################
## Date time module 
######################
import datetime
#example 1 
t = datetime.time(5,25,1)
print t.hour #a lot method you can call

#example 2
today = datetime.date.today()
print today

#example 3
d1 = datetime.date(2015,3,11)
print d1
d2 = d1.replace(year=1990)
print d2
dtime = d1 - d2
print dtime

######################
## Python Debugger  
######################
import pdb
x = [1,2,3,4,5]
y = 222
z = 12
pdb.set_trace() #when run, will stop here, you can interact with variables 
result = z+y
result2 = x + y
print result2

######################
## regular expression module  
######################



