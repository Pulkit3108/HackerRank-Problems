#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    x=len(arr)
    a=0
    b=0
    c=0
    for i in range(0,x):
        if(arr[i]>0):
            a=a+1
        if(arr[i]<0):
            b=b+1
        if(arr[i]==0):
            c=c+1
    print(float(a)/float(x))
    print(float(b)/float(x))
    print(float(c)/float(x))

    #
    # Write your code here.
    #

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
