class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

e=Employee("sony",12345)
print(e.name)
print(e.sal)

#not to dispaly salaru to other...    use double underscore.
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.__sal=sal

e=Employee("sony",12345)
print(e.name)
