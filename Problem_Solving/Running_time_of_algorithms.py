import sys
n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
count=0
if(a==b):
    print("0")
    sys.exit()
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while(a[j]>key and j>=0):
        a[j+1]=a[j]
        j=j-1
        count=count+1
    a[j+1]=key
print(count)
