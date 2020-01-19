#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort(reverse=True)
    count2=0
    count1=0
    for i in range(0,len(a)):
        count1=1
        for j in range(i+1,len(a)):
            if((a[i]-a[j])<2):
                count1=count1+1
        count2=max(count1,count2)
    return(count2)


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
