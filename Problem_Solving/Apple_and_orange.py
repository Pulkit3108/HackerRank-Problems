#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(0,len(apples)):
        apples[i]=apples[i]+a
    for i in range(0,len(oranges)):
        oranges[i]=oranges[i]+b
    c1=0
    c2=0
    for i in range(0,len(apples)):
        if(apples[i]>=s and apples[i]<=t):
            c1=c1+1
    for i in range(0,len(oranges)):
        if(oranges[i]>=s and oranges[i]<=t):
            c2=c2+1
    print(c1)
    print(c2)

if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)
