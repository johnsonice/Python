########################
#######Python Statemsents
##########################

######
##if statements
######

user = 'Johnson'

if user == 'Chengyu' or 'Johnson':
    print 'Welcome Chengyu'
elif user == 'Tony':
    print 'Welcome Tony'
else:
    print "You don't have access"

#######
#For loops
#######

l = [1,2,3,4,5,6]
r = [] #result 
for ele in l:
    m = ele % 2
    if m == 0:
        r.append('even') 
    else:
        r.append('odd')
print r
    #example 2
l = [(2,4),(6,8),(10,12)]
    #tup unpacking while writing for loop 
for (t1,t2) in l: 
    print t1 + t2
    #example 3
d = {'k1':1,'k2':2,'k3':3}
for k,v in d.iteritems():
    print "{k}: {v}".format(k=k, v=v)

#######
#while loops
#######
x = 0
while x < 10:
    print 'x is currently: ', x
    x +=1
else:
    print 'All Done'
######
#break and continue
######
x = 0
while x < 10:
    print 'x is currently: ', x, ', add one to x '
    x +=1
    if x ==3:
        print 'Hey, x equals to 3!'
        break #break the outer loop
    else:
        print 'continueing...'
        continue #stop inner loop, continue outter loop 
else:
    print 'All Done'


#######
#range() and generators
#######
    #example 1
start = 5
stop = 20
step = 3
x = range(start,stop,step) #generate a list form 5 to 20 step 3
type(x) # will tell you it is a list
#usage
for num in xrange(1,1000,10): #xrange will not store range in memory
    print num

#example 2 -- create generator function use yield
    #it will automatic generage something like a list, but will save memory
def genfibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        t = a
        a = b
        b = t+b
for num in genfibon(10):
    print num
#########user iterables 
s = 'hello'
s_iter = iter(s)
print next(s_iter)




########
#Comprehensions
########
lst = [letter for letter in 'word']
print lst

lst = [x**2 for x in xrange(0,11)]
print lst

lst = [number for number in xrange(11) if number %2==0]
print lst

celsius = [0,10,20.1,34.5]
fahrenheit = [(temp*(9/5.0) + 32) for temp in celsius ]
print fahrenheit

lst = [x**2 for x in [x**2 for x in range(11)]] #nested comprehensions 
print lst #x**4

