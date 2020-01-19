#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

from math import gcd

def getTotalX(a, b):
    a1=a[0]
    b1=b[0]
    for i in range(1,len(a)):
        a1=int((a1*a[i])/gcd(a1,a[i]))
    for j in range(1,len(b)):
        b1=int(gcd(b1,b[j]))
    count=0
    for x in range(a1, b1+1, a1):
        if gcd(x, b1) == x:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
