# file=open("test.txt","r")
# f=file.read()
# print(f)
# file=open("test.txt","w")
# file.write("hello himanshu\n")
# file.write("Whats up bro?")
#file=open("test.txt","r")
# f=file.read()
# print(f)
#file.close()
#x=["a","b","c","d","e"]
file=open("test.txt","w")
x=["ab","bfhjs","cdsdew","d","e"]
for item in x:
    print(file.write(item + "\n"))
file.close()
file=open("test.txt","r")
f=file.read()
print(f)