#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    x=len(arr)
    a=0
    b=0
    for i in range(0,x):
        for j in range(0,x):
            if(i==j):
                a=a+arr[i][j]
            if(i+j==x-1):
                b=b+arr[i][j]
    y=abs(a-b)
    return y


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
