#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    new = 0
    k = k % 26
    newstr = ""
    for i in range(0,len(s)):
        if (ord(s[i]) > 96 and ord(s[i]) < 123 - k or ord(s[i]) > 64 and ord(s[i]) < 91-k):
            new = ord(s[i]) + k
            newstr+=chr(new)
        elif (ord(s[i])>122-k and ord(s[i]) < 123 or ord(s[i]) > 90-k and ord(s[i]) < 91):
            new = ord(s[i]) - 26 + k
            newstr+=chr(new)
        else:
            newstr+=s[i]
    return newstr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
