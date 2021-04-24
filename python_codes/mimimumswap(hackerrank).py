#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0
    i = 0
    
    while i < n-1:
        
        if arr[i] == i + 1:
            i += 1
            
        else:
            #arr[arr[1]-1],arr[1]=arr[1],arr[arr[1]-1]
            #arr[3-1],arr[1]=arr[1],arr[3-1]
            #arr[2],arr[1]=arr[1],arr[2]
            #3,2=2,3 (swaping tech)
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            res += 1
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
