#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    big = max(ar)
    for i in range(len(ar)):
    
        if(ar[i]==big):
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
