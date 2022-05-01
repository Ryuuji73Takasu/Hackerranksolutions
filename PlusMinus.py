import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = []
    negative = []
    zero = []
    
    for i in arr:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zero.append(i)
    
    print("{:.6f}".format(len(positive)/len(arr)))
    print("{:.6f}".format(len(negative)/len(arr)))
    print("{:.6f}".format(len(zero)/len(arr)))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
