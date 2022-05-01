#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if(s[8] =='P'):
        a = int(s[0]+s[1])
        if (a < 12):
            a += 12
        s = s.replace(s[0]+s[1],str(a))
        s = s.replace("PM","")
        return s
    else:
        s = s.replace("AM","")
        a = int(s[0]+s[1])
        if (a >= 12):
            a -= 12
        if a < 12:
            a = str(a)
            a = a.zfill(2)
        s = s.replace(s[0]+s[1],str(a)) 
        return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
