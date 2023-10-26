'''
class

// built-in class attributes
# __dict__   dictionary
# __doc__   docstrings
# __name__  class name
# __module__    used to acess the class in which module is defined.
# __init__



object

inheritance
single level
mmulti level
multiple

encapsulation

polymorphism
overloading
overriding

reusability

constructor
destructor

'''
'''
# parametrized  constructor.
class person:
    def __init__(self,name):   #definition of constructor.  and created a parameter name. 'self' is reference and 'name' is parameter/variable.
        self.name=name  #this.name = name

p=person("himanshu")   # object for class. passing a value. ----when we create an object for line 26 ....line 23 also get invoked.
print(p.name)   #p persnon=new person()
print("value of builtin variable name is ",__name__)



#default constructor

class person:
    def __init__(self):
        print("I am default construcotr")
p=person()
print(p)

######################
def main():
    print("hi")
main()


def main():
    print("hello")
main()
print("value of builtin variable name is ",__name__)    #__name__ gives module name or the code is implemented from main.


def main():
    print("hi there")
if __name__=="__main__":
    main()


class person:
    def __init__(self, id, name):
        self.id=id
        self.name=name
p1=person(1,"himanshu")
print(p1.id,p1.name)

#another method

class person:
    id=2
    name="himanshu"

    def display(self):      #without self reference we cannot read.
        print(self.id, self.name)
p=person()
p.display()


class person:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print('my name is ', self.name, 'my id is ',self.id)
p=person('ganesh', 3)
p1=person('piyu',4)
p.display()
p1.display()
#to update--
p.id=5
p.display()

'''
'''
#DESTRUCTOR

#DELETE THE ATTRIBUTE FROM CLASS OR FUNCTION.
class person:
    """ACCESS THE COMMENT"""
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print('my name is ', self.name, 'my id is ',self.id)
p=person('ganesh', 3)
del p.id
p.display()

'''

# SHOWING THE COMMENT---
class person:
    """HIDING THE COMMENT"""
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print('my name is ', self.name, 'my id is ',self.id)
p=person('ganesh', 3)
p.display()


class person:
    """showing THE COMMENT using doc"""
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print('my name is ', self.name, 'my id is ',self.id)
p=person('ganesh', 3)
p.display()
print(p.__doc__)    #showing the comment
print(p.__dict__)   #key- value format
print(p.__module__) 
print(p.__init__)
