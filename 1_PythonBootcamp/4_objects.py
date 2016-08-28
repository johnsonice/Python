###################################
#####Object orientate Programming #
###################################

###################
# create an object
###################

class Circle(object):
    #class Object Attribute
    pi = 3.14
    #object properties 
    def __init__(self,radius=1): #set the default to be 1
        self.radius = radius
        self.perimeter = self.get_perimeter()
        print 'New circle created'
    #methods
    def area(self):
        return self.radius**2 * Circle.pi #pi is a class object att

    def set_radius(self, new_radius):
        """
        set radius to new value
        """
        self.radius= new_radius
        self.perimeter = self.get_perimeter() #when radius changes, perimeter changes as well

    def get_radius(self):
        return self.radius

    def get_perimeter(self):
        return 2*Circle.pi*self.radius
    
# now call properties 
c = Circle(radius=100)
c.area() #call area method
c.set_radius(20) #change the radius 
c.get_radius()
c.perimeter

############
##inherient
############
class Animal(object):
    def __init__(self):
        print "New Animal created"

    def whoAmI(self):
        print "I am an animal"

    def eat(self):
        print "Eating"

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print 'Dog'

    def bark(self):
        print "woof!"

d=Dog()
d.whoAmI() #base class method get overwriten 
d.eat() #can call inherient method

############
##special class
############
class Book(object):
    def __init__(self,title,author,pages):
        print "A book has been created!"
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: %s, Author: %s, pages %s" %(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print "A book is gone!"
        
b=Book('Python','Jose',100)
print b  #it will print content in __str__
print len(b) #return length of the pages 
del b #will print book is gone


