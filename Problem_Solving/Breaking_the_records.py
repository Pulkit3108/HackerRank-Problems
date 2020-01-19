#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    count1=0
    count2=0
    max=scores[0]
    min=scores[0]
    for i in range(0,len(scores)):
        if(scores[i]>max):
            count1=count1+1
            max=scores[i]
        if(scores[i]<min):
            count2=count2+1
            min=scores[i]
    return(count1,count2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
