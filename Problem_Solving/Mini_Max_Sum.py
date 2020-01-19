#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    x=len(arr)
    max=arr[0]
    min=arr[1]
    for i in range(0,x):
        if(arr[i]>max):
            max=arr[i]
        if(arr[i]<min):
            min=arr[i]
        
    a=0
    for i in range(0,x):
        a=a+arr[i]
    print(a-max,a-min)
        
    #
    # Write your code here.
    #

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
