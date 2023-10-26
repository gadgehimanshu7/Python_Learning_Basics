'''
Loops in python:
    1.for
    2.while

    break
    continue

    range()

'''
'''
x=[0,1,2,3,4,5,6,7,8,9]

for i in x:

    x[i] = input("Enter something")

print(x)

'''

'''
y=[1,2,3]

for i in y:

    y[i]=input("Enter purpose")
print(y)
'''

#NESTED:

x=['a','b','c','d','e']
y=['1','2','3','4','5']

for i in x:
    for j in y:
        print(x,y)



x=['a','b','c','d','e']
y=['1','2','3','4','5']

a=0;
b=0;
for i in x:
    for j in y:
        print(x,y)
        b +=1
    a+=1
    b=0 
