# method Overriding
class printMyName:
    def __init__(self):
        print("Instantiating")

    def printDetails(self):
        print("Merry Christmas")

class printFullDetails(printMyName):
    def printDetails(self):
        print("Merry christmas is on sunday.")

p=printFullDetails()
p.printDetails()



# operator Overloading

class Demo:
    def __init__(self, a):
        self.a = a

    # adding 2 objects
    def __add__(self, o):
        return self.a + o.a



d = Demo(5)
d1 = Demo(10)
print(d + d1)
d2 = Demo(2.3)
d3 = Demo(5.6)
print(d2 + d3)
d4 = Demo("Accenture")
d5 = Demo("cloud")
print(d4 + d5)
