#!/bin/python3

import math
import os
import random
import re
import sys


def reverse(n):
    s=0
    while(n!=0):
        r=int(n%10)
        n=int(n/10)
        s=int(s*10+r)
    return(s)

a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)
count=0
for i in range(a,b+1):
    if(abs(i-reverse(i))%c==0):
        count=count+1
print(count)
