import math,random

n=4
m=3
a=[]

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(-3,7))

def collumn_find(lis):
    collumn_sum=0

    for i in range(n):
        for j in range(m):
            collumn_sum+=lis[i][j]
        if collumn_sum<0:return i 
    return -1
        
x= collumn_find(a)

if x==-1:
    print("There is no collumn sum with -")
else:
    print(f"The collumn with - sum index is :{x}")