#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    count=0
    c=c+[0]
    while i !=(n-1):
        if(c[i+2]==0 and i<(n-2)):
            i+=2
            count+=1
        else:
            i+=1
            count+=1
    return count            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
