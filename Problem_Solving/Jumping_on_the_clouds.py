#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n=len(c)
    e=100
    i=0
    i=(i+k)%n
    while(i!=0):
        if(c[i]==1):
            e=e-3
        elif(c[i]==0):
            e=e-1
        i=(i+k)%n
    if(c[0]==1):
        return(e-3)
    elif(c[0]==0):
        return(e-1)
    
        
   



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
