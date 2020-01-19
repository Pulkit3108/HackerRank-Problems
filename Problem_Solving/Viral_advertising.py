import math
a=int(input())
count=math.floor(5/2)
x=math.floor(5/2)*3
for i in range(0,a-1):
    count=count + math.floor(x/2)
    x=math.floor(x/2)*3
print(count)
