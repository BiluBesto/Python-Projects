#!/bin/python

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'ticketCounterWithPatience' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY times
#  2. INTEGER k
#

def ticketCounterWithPatience(times, k):
    q=deque()
    for i,t in enumerate(times):
        q.append([i,t])
    result=[]
    while q:
        index,val=q.popleft()
        if val<=k:
            result.append(index)
        else:
            val-=k
            q.append([index,val])
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(raw_input().strip())

    inputTime = map(int, raw_input().rstrip().split())

    K = int(raw_input().strip())

    result = ticketCounterWithPatience(inputTime, K)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
