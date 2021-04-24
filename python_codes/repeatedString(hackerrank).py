#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num = s.count('a')
    if num == 0:
        return 0
    elif num == 1 and len(s)==1:
        return n
    else:
        repeats = n/len(s)
        rem = n%len(s)
        return str(num*repeats+s[:rem].count('a')) 
          
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
