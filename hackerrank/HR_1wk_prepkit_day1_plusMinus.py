#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    pos_nums = []
    neg_nums = []
    zero_digits = []
    # Write your code here
    for e in arr:
        if e == 0:
            zero_digits.append(n)
        elif e > 0:
            pos_nums.append(n)
        elif e < 0:
            neg_nums.append(n)
    # # Also,
    # positive_count = 0
    # negative_count = 0
    # zero_count = 0
    #
    # for num in arr:
    #     if num > 0:
    #         positive_count += 1
    #     elif num < 0:
    #         negative_count += 1
    #     else:
    #         zero_count += 1

    positive_ratio = len(pos_nums) / len(arr)
    neg_ratio = len(neg_nums) / len(arr)
    zero_ratio = len(zero_digits) / len(arr)
    # map(str, [positive_ratio, neg_ratio, zero_ratio])
    # lambda x: str(round(x,6))
    # final_ratios = "".join(map(lambda s: str(round(s, 6)),
    #                             [positive_ratio, neg_ratio, zero_ratio]))
    # formatted_numbers = [format(num, '.6f') for num in float(final_ratios)]
    final_ratios = "\n".join(map(lambda s: str(format(s, '.6f')),
                                    [positive_ratio, neg_ratio, zero_ratio]))
    print(final_ratios)


if __name__ == '__main__':
    # n = int(input().strip())
    n = 6
    # arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
