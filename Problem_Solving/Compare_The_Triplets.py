#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    total_a = 0
    total_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            total_a = total_a + 1
        elif a[i] < b[i]:
            total_b = total_b + 1
    return (total_a, total_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
