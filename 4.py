##python program to sort dictionary

import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
a=[]
b=[]
empty={}
for i in d.keys():
    a.append(i)
a.sort()
for j in d.values():
    b.append(j)
b.sort()
for i in range(0, len(a)):
    empty[a[i]]=b[i]
print(empty)




