'''
x=input("your name?\n")
print(x)

y=input("number 1: ")
y=int(y)                            #type 1
z=input("number 2: ")
z=int(z)

result=y+z
print(result)   #input() takes input as string and not as integer. so answer is 45 but not 9.

#to take inoput value as int......
res=y+z
print(res)

#####or#####

res=int(y)+int(z)
print(res)                          #type 2


'''
'''
def add(x,y):
    x=int(x)
    y=int(y)
    z=x+y
    print(z)

add(1,2)

a=4
b=8
add(a,b)
'''

#other way

'''
def add(x,y):
    z=x+y
    z=x**y   #power
    print(z)

a=input("enter the first value")
a=int(a)
b=input("enter the 2nd value")
b=int(b)
add(a,b)
'''

#COnvertors using function.
'''
def celcius(c,f=0):
    f=(9/5)*c +32
    print(f)

def far(f,c=0):
    c=f*(5/9)-32
    print(c)

a=input("temp in celcius")
a=int(a)
celcius(a)
b=input("temp in farenheit")
b=int(b)
far(b)
'''

#Modification of FUNCTION.
'''
def div(a,b):
    if(b==0):
        print("dividend cannot be ZERO")
    else:
        c=a/b
        print(c)

a=input("enter 1st value")
a=int(a)
b=input("enter 2nd value")
b=int(b)
div(a,b)

#div(int(a),int(b))
'''

'''
def studScore(name,score):
    print(name)
    print(score)

studScore('himanshu',100)


def studScore(name,*score):    # '*' can only be used to last variable.
    print(name)
    print(score)

studScore('himanshu',100,45,6,7,88)

'''

# Anonymous function:- LAMBDA

sum= lambda x : x +10
print(sum(3))

s= lambda x,y : x * y
print(s(4,5))

myList=[10,2,3,4,5,56,7]
x= lambda myList: myList*2      # it will multiply only one value. wrong answer.
print(x)


myList=[10,2,3,4,5,56,7]
print(list(map(lambda x: x*2, myList)))

print(list(filter(lambda x:x%2==0, myList)))

print(list(filter(lambda x:x%2==1, range(1,20))))
