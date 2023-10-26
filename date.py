import datetime

x=datetime.datetime.now()   #print present time.
y=datetime.datetime(2060,3,18)
print(x)
print(y)
print(x.year)
print(x.month)

x=datetime.datetime.now()
print(x.strftime("%w"))     #day of week.
print(x.strftime("%p"))     #PM.
