n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split()))
a=[0]*10001
b=[]
for i in range(0,len(arr)):
    a[arr[i]]=a[arr[i]]-1
for j in range(0,len(brr)):
    a[brr[j]]=a[brr[j]]+1
for k in range(0,len(a)):
    if(a[k]>0):
        b.append(k)
print(' '.join(map(str,b)))


        



