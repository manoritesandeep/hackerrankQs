"""
collections.OrderedDict

An OrderedDict is a dictionary that remembers the order 
    of the keys that were inserted first. 
If a new entry overwrites an existing entry, 
    the original insertion position is left unchanged. 



"""
# Example
from collections import OrderedDict
import io
import sys
from collections import OrderedDict

ordinary_dictionary = {}
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5

print(ordinary_dictionary)
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}

ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5

print(ordered_dictionary)
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# Task
# You are the manager of a supermarket. 
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

sample_input = '''9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30'''

# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

num_items = int(input())

# Read the items and their prices into a list of tuples
# s = "BANANA FRIES 12"
# item, price = s.rsplit(' ', 1)
# print(item, price)
item_details = [input().rsplit(" ", 1) for _ in range(num_items)]
print(num_items)
print(item_details) 
# [['BANANA FRIES', '12'], ['POTATO CHIPS', '30'], ['APPLE JUICE', '10'], ['CANDY', '5'], ['APPLE JUICE', '10'], ['CANDY', '5'], ['CANDY', '5'], ['CANDY', '5'], ['POTATO CHIPS', '30']]

# Create an ordered dictionary to store the items and their prices
ordered_items = OrderedDict()
# Iterate through the list of items and their prices
for item, price in item_details:
    # If the item is not in the ordered dictionary
    if item not in ordered_items:
        # Add the item to the ordered dictionary with the price as the value 
        ordered_items[item] = int(price)
    else:
        ordered_items[item] += int(price)
print(ordered_items)

for item, price in ordered_items.items():
    print(item, price)
