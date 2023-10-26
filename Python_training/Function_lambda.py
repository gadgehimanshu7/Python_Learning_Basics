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
