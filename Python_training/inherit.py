#have two classes
#   a. parent class
'''
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printName(self):
        print(self.fnmane, self.lname)

p=Person("himanshu", "gadge")
p.printName()
'''

#   b. child class
'''
class Person:       #parent class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printName(self):
        print(self.fname, self.lname, self.year)

class Student(Person):          #child class
    def __init__(self,fname,lname,year):
        Person.__init__(self,fname,lname)   #taking from person class
        self.year=year
s=Student("priyank","chavhan",2020)
s.printName()
print(s.year)
# p=Person("himanshu", "gadge")
# p.printName()
'''


#Multiple Inheritance

class Parent:
    def m(self):
        print("I am parent class")

class Child:
    def n(self):
        print("I am child class")

class gCHild(Parent,Child):
    pass

c=Child()
c.n()
