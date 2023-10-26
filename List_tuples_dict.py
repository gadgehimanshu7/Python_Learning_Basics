"""

#Lists


x=['a','b','c','d',4,7,8.9]
print(x)
print(x[2])
print(x[-2])
print(len(x))
print(x.pop())
print(x)
x.append(9)
print(x)
x.pop(2)   #x.remove("c")
print(x)
x.insert(3,'h')
print(x)



#Tuples

x=()  #tuples ....elements cannot be changed.
x=[]  #lists
x=""  #strings

x=('a','b','c','d','h') #accessing same like list.
print(x[2])
print(x[-2])
print(len(x))
print(dir(tuples))

"""

#DICTONARY

x=()  #tuples ....elements cannot be changed.
x=[]  #lists
x=""  #strings
x={} #Dictonary
x={"number":1,"name":"Himanshu","age":22}
print(x["name"])
x["address"]="pune"
print(x)
x.pop("number")
x["age"]=25
print(x)
x.popitem()
print (x)



'''
complex(2 ,4)
(2+4j)
>>> x=5
>>> str(5)
'5'
>>> str(x)
'5'
>>> y=[1,2,3,4,5]
>>> y
[1, 2, 3, 4, 5]
>>> tuple(
... y)
(1, 2, 3, 4, 5)
  set(y)
{1, 2, 3, 4, 5}
>>> t="T"
>>> ord(t)
84
>>>

'''
