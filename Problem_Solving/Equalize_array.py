#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    count=0
    k=0
    for i in range(0,len(arr)):
        count=0
        for j in range(i,len(arr)):
            if(arr[j]==arr[i]):
                count=count+1
            k=max(k,count)
    return(len(arr)-k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
