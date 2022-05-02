#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    n = len(a)
    if (n==1):
        return a[0]
    if a[n-1] != a[n-2]:
        return a[n-1]
        
    for i in range(0,len(a),2):
        if a[i] != a[i+1]:
            if (a[i+1]==a[i+2]):
                return (a[i])
            else:
                return (a[i+1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
