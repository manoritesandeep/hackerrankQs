#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np
import random

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
import collections


def countingSort(arr):
    # Write your code here
    # print(arr)
    # check for non-negative ints
    if any(val < 0 for val in arr):
        raise ValueError("Input array is negative... check input")

    freq = [0] * 100
    for val in arr:
        # if value in array, increase freq of value by 1
        freq[val] += 1
    return freq


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    n = 100
    # arr = list(map(int, input().rstrip().split()))
    # arr = random.randint(0,100)
    # arr = [random.randint(0,101) for _ in range(100)]
    arr = [87, 42, 95, 61, 30, 16, 74, 98, 34, 83, 52, 2, 40, 80, 53, 77, 56, 63, 84, 23, 13, 92, 47, 79, 41, 68, 71,
           29, 72, 36, 33, 26, 39, 64, 7, 57, 60, 31, 73, 44, 89, 69, 35, 6, 38, 21, 65, 75, 58, 94, 45, 76, 91, 96,
           66, 99, 88, 50, 93, 48, 20, 17, 24, 55, 97, 70, 4, 5, 82, 86, 11, 15, 81, 67, 51, 10, 14, 85, 1, 8, 12, 3,
           19, 9, 18, 25, 62, 28, 37, 59, 27, 49, 22, 43, 78, 32, 90, 54, 46]
    result = countingSort(arr)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
