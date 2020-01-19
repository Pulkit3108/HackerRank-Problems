import math
import sys
n=int(input())
a=list(map(int,input().split()))
b=[]
a.sort()
diff=sys.maxsize
for i in range(0,len(a)-1):
    if(diff>(a[i+1]-a[i])):
        diff=a[i+1]-a[i]
for i in range(0,len(a)-1):
    if(diff==a[i+1]-a[i]):
        b.append(a[i])
        b.append(a[i+1])
print(' '.join(map(str,b)))

