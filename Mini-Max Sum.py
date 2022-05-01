#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    summ = 0
    anotherarr=arr[:]
    del anotherarr[len(anotherarr)-1]
    del arr[0]
    for i in anotherarr:
        summ += i
    
    summm = 0
    for i in arr:
        summm += i
    print(str(summ)+" " +str(summm))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
