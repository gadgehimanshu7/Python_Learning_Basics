
'''
a=90
b=7
if(a,b==0):
    print("a,b is smaller")
else:
    print("a is biger")
'''
'''
import os
print(os.getcwd())  #get current working directory
print(os.path.getsize('/Users/himanshugadge/Desktop/python/first.py'))  #file size
print(os.path.isfile('/Users/himanshugadge/Desktop/python/Second.py'))    #check if file is present in directroy or path

#os.mkdir('/Users/himanshugadge/Desktop/python/demo')    #create folder or directory.
#os.rmdir('/Users/himanshugadge/Desktop/python/demo')    #remove directory or folder
#os.unlink('/Users/himanshugadge/Desktop/python/text.rtf')   #remove file
#os.unlink('/Users/himanshugadge/Desktop/python/Stringcopy.py')
help(os) #details

'''

'''FILE HANDLING'''
'''
#read FILE
fileObj=open('/Users/himanshugadge/Desktop/python/Errors.txt','r')      #r= read()
print(fileObj.read())
myList=fileObj.readlines()
print(myList)
#for i in myList:
    #print(i)
fileObj=open('/Users/himanshugadge/Desktop/python/hima.txt','w+')        #w+='+' for write first time
print('file created')                                                       #w= write
lst = ['BDC','cdc','mdc']
fileObj.writelines(lst)
print('data written')
fileObj.close()

fileObj=open('/Users/himanshugadge/Desktop/python/hima.txt','a')        #a=append data without disturbing previous data.
#print('file created')
lst = ['abc ','bdc \n','cdc']
fileObj.writelines(lst)
print('data appended')
fileObj.close()

# fileObj=open('/Users/himanshugadge/Desktop/python/hima.txt','w')        #w- over write data.
# #print('file created')
# lst = ['ghj\n','fgv\n','mdc']
# fileObj.writelines(lst)
# print('data written')
# fileObj.close()

newObj=open('/Users/himanshugadge/Desktop/python/demo1.txt','w')
newList2=['A' , 'B']
newObj.writelines(newList2)
newObj.close()

'''

'''CSV FILE'''

import csv

#import os
#os.unlink('/Users/himanshugadge/Desktop/python/newfile.csv')
# fileObj = open('/Users/himanshugadge/Desktop/python/newfile.xls','w+')
# print('excel file created')
# fileObj.close()
myFile = open('/Users/himanshugadge/Desktop/python/newfile.xls','r')
# r=csv.reader(myFile)      #reader
# data= list(r)
# print(data)
print(myFile.read())


myFile = open('/Users/himanshugadge/Desktop/python/newfile.xls','a+')
print('file opened')
w=csv.writer(myFile)    #writer
w.writerow(['5','ajya','bang'])
print('data updated')
myFile.close()

myFile = open('/Users/himanshugadge/Desktop/python/newfile.xls','r')
print(myFile.read())
