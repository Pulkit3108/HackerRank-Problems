from itertools import combinations
N=int(input())
A=list(input().split())
K=int(input())
C=list(combinations(A,K))
count=0
for i in C:
    if('a' in i):
        count=count+1
print(count/len(C))
