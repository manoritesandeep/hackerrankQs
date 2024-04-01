"""
A newly opened multinational brand has decided to base their company logo on the three and
most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. 
Given a string s, which is the company name in lowercase letters, your task is to find the top 
three most common characters in the string.

    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count.
    If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G,O,E.
"""

from collections import Counter
import sys
import io

# sample_input = """aabbbccde"""
sample_input = """google"""

# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

word_ls = [w for w in sample_input]
# print(word_ls)

word_count = Counter(word_ls)
# print(type(word_count))
# print(word_count)

# Sort the items of the Counter by count in descending order and then by key in ascending order
sorted_items = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
print(sorted_items)

# Use most_common() to get a list of elements and their counts, sorted by the count
# Reverse the list to sort in ascending order - eg: reversed(word_count.most_common())
for word, count in sorted_items[:3]:
    # print(word, count)
    print(word)




