#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s=0
    k1=0
    for i in range(0,len(bill)):
        s=s+bill[i];
    k1=int((s-bill[k])/2)
    if(k1==b):
        print("Bon Appetit")
    else:
        print(int(bill[k]/2))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
