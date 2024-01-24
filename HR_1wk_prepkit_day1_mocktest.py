#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    length = len(sorted_arr)
    middle_index = length // 2

    if length % 2 == 0:
        median = (sorted_arr[middle_index - 1] + sorted_arr[middle_index]) / 2
    else:
        median = sorted_arr[middle_index]

    return median


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

## Method 2:
import statistics

data = [5, 2, 9, 1, 7, 4, 6, 3, 8]
median = statistics.median(data)

print(median)
