#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    count =0
    count1=0
    count2=0 
    
    for j in range(len(note)):
            
              if note[j] not in magazine:
                count1+=1
                
              else:
                if(note.count(note[j])>=2):
                        count2+=1
    if count1 ==0 and count2==0:
        print("Yes")
    else:
        print("No")     
    
                       
if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
