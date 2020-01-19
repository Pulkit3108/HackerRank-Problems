from collections import Counter
X=int(input())
c=list(map(int,input().split()))
N=int(input())
income=0
size=Counter(c)
for i in range(0,N):
    a,b=map(int,input().split())
    if size[a]: 
        income+=b
        size[a]-=1

print(income)
