#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = 22

    if n % 2 != 0:
        print("Oddly_Weird")
    elif n in range(2, 6) and (n % 2) == 0:
        print("Evenly_Not Weird")
    elif n in range(6, 21) and n % 2 == 0:
        print("6-21 Weird")
    elif n > 20 and n % 2 == 0:
        print("Over 20 Not Weird")
    else:
        print('Not valid')



if __name__ == '__main__':
    n = 22

    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6) and (n % 2) == 0:
        print("Not Weird")
    elif n in range(6, 21) and n % 2 == 0:
        print("Weird")
    elif n > 20 and n % 2 == 0:
        print("Not Weird")
    else:
        print('Not valid')
