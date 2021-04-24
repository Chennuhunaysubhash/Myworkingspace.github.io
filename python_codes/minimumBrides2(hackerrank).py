#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
     moves = 0
     for i in range( n-1, -1, -1): 
        if ( q[i]  -  (i+1) )  >  2:
            print("Too chaotic")
            return
       
        for j in range( max(0, q[i]-2), i,  1):
            
            if q[j] > q[i] :
                moves+=1 
            
     print(moves)     

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
