import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(sample_arr):
    # Write your code here
    sum_min_nums = sum(sorted(sample_arr)[:-1])
    # print(sum_min_nums)
    sum_max_nums = sum(sorted(sample_arr)[1:])
    print(sum_min_nums, sum_max_nums)


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    sample_arr = [1, 2, 3, 4, 5]
    miniMaxSum(sample_arr)
