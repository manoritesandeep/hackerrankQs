"""
collections.deque()

A deque is a double-ended queue. 
It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and 
    pops from either side of the deque with approximately the same O(1)
    performance in either direction.

"""


from collections import deque
import io
import sys

# d = deque()
# d.append(1)
# print(d) # deque([1])
# d.appendleft(2)
# print(d) # deque([2, 1])
# d.clear()
# print(d) # deque([])
# d.extend('1')
# print(d) # deque(['1'])
# d.extendleft('234')
# print(f"Extend left: {d}") # deque(['4', '3', '2', '1'])
# d.count('1') # 1
# d.pop() # '1'
# print(d) # deque(['4', '3', '2'])
# d.popleft() # '4'
# print(d) # (['3', '2'])
# d.extend('7896')
# print(d) # deque(['3', '2', '7', '8', '9', '6'])
# d.remove('2')
# print(d) # deque(['3', '7', '8', '9', '6'])
# d.reverse()
# print(d) # deque(['6', '9', '8', '7', '3'])
# d.rotate(3)
# print(d) # deque(['8', '7', '3', '6', '9'])

sample_input = '''6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''

# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

num_operations = int(input())
methods = [input().split() for _ in range(num_operations)]
print(methods)
# ['append 1', 'append 2', 'append 3', 'appendleft 4', 'pop', 'popleft']

d = deque()
## d.rotate(3)
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])
