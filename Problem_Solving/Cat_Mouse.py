
#!/bin/python3

import math
import os
import random
import re
import sys

q = int(input().strip())
for a0 in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]

    absCatA, absCatB = abs(x - z), abs(y - z)

    if absCatA == absCatB:
        print("Mouse C")
    else :
        print ("Cat A" if absCatB > absCatA else "Cat B")
