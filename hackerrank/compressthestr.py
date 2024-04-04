"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . 
To read more about this function, 
    Check this out https://docs.python.org/2/library/itertools.html#itertools.groupby.

You are given a string S. 
Suppose a character 'c' occurs consecutively times in the string. 
Replace these consecutive occurrences of the character 'c' with (X,c) in the string. 

"""

from itertools import groupby
import sys
import io

sample_input = "1222311"


# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

# unique_keys = [k for k,g in groupby(sample_input)]
# print(unique_keys)
# g = [list(g) for k,g in groupby(sample_input)]
# print(g)

# Use groupby() to group the input by consecutive identical elements
# For each group, output a tuple with the count and the element
compressed_str = [(len(list(g)), k) for k,g in groupby(sample_input)]
# print(compressed_str)
print(*compressed_str, sep=' ')
