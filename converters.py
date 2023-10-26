#c = input("temp in celcious")
#f = (9/5) * c +32
#print(f)


'''
 this will show an error as

f = (9/5) * c +32
TypeError: can't multiply sequence by non-int of type 'float'

as 9/5 is float and c is not declared as type.

'''

c = input("temp in celcious")
c = int(c)
f = (9/5) * c +32
print(f)
#or
print(int(f))

m=input("Enter in minutes")
s=input("Enter in seconds")
h=int(m)/60 + int(s)/3600
print(h)
