#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from datetime import datetime


def timeConversion(s):
    # Write your code here
    # Convert the input time string to a datetime object
    # %I: Represents the hour in 12-hour format (01 to 12).
    # :: Represents a colon separator.
    # %M: Represents the minute (00 to 59).
    # %S: Represents the second (00 to 59).
    # %p: Represents the AM/PM indicator.
    time_obj = datetime.strptime(s,
                                 "%I:%M:%S%p")

    # to military time
    # %H: Represents the hour in 24-hour format (00 to 23).
    # :: Represents a colon separator.
    # %M: Represents the minute (00 to 59).
    # %S: Represents the second (00 to 59).
    mil_time = datetime.strftime(time_obj,
                                 "%H:%M:%S")
    return mil_time


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s_sample = "07:05:45PM"
    result = timeConversion(s_sample)
    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
