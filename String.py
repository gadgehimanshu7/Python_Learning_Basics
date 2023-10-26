
x='water'
print(x[1])   #indexing
#print(x[6]) #string index out of range
x=x.replace('w' , 't')
print(x)
x='my name is himanshu'
print(x.split())
print(x.split('is'))
print(x[1:8])  #slicing
print(x[11:19])
print(x[-2])
print(x[-8:-5])
print(x[:3])        #x[0:3]
print(x[::-1])    #reverse string till end.

#string formatting

x='MY '
y='NAME '
z='IS '
v='HIMANSHU'
w=x+y+z+v
print(w)

x='my name is'
y='himanshu'
z='my name is {}'.format(y)
print(z)


x=22
y="HIMANSHU"
z='my name is {} and my age is {}'.format(x,y)
print(z)
z='my name is {1} and my age is {0}'.format(x,y)
print(z)
z='my name is {y} and my age is {x}'
print(z)
z=f'my name is {y} and my age is {x}'
print(z)
x=['hima','badminton','22']
z=f'my name is {x[0]},.nmy age is {x[2]},.ni play {x[1]}'
print(z)
