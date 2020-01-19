from itertools import permutations
S,k=input().split()
k=int(k)
for i in list(permutations(sorted(S),k)):
    print(''.join(i))
