from collections import Counter, OrderedDict
import io
import sys


sample_input = '''4
bcdef
abcdefg
bcde
bcdef
'''

# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

n = int(input())
print(type(sample_input))
# print(sample_input.split())

words = [input().strip() for _ in range(n)]
print(words)
# ['bcdef', 'abcdefg', 'bcde', 'bcdef']
print(OrderedDict(Counter(words)))
print(f"Number of distinct words: {len(OrderedDict(Counter(words)).keys())}")
print(f"Number of occurrences for each distinct word according to their appearance in the input:{list(OrderedDict(Counter(words)).values())}")


print(len(OrderedDict(Counter(words)).keys()))
print(*list(OrderedDict(Counter(words)).values()))
