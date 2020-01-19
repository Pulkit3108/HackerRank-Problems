#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    # Write your code here.
    
    for i in range(0,n):
        for j in range(0,n):
            if(i+j<n-1):
                print(" ",end='')
            else:
                print("#",end='')
        print(" ")
        
        

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
