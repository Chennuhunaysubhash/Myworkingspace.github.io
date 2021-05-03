#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    flag = True
    c1 = Counter(magazine)
    c2 = Counter(note)
    for k , v in c2.items():
        if k in c1 and c1[k]>=v:
            continue
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")        
            

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
