"""
There is a horizontal row of cubes. 
The length of each cube is given. 
You need to create a new vertical pile of cubes. 
The new pile should follow these directions: 
    if cube[i] is on top of cube[j] then
    sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example
blocks=[1,2,3,8,7]
Result: No

After choosing the rightmost element, 7, 
    choose the leftmost element, 1. 
After than, the choices are 2 and 8. 
These are both larger than the top block of size.

blocks = [1,2,3,7,8]
Result: Yes

Choose blocks from right to left in order to successfully stack the blocks. 

"""
import sys
import io
from collections import deque

sample_input = """2
6
4 3 2 1 3 4
3
1 3 2
"""
# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

# num_test_cases = int(input())
# num_cubes = int(input())
# cube_block = list(map(int, input().split()))
# cube_blocks = [input().split() for _ in range(num_test_cases)]
# print(num_test_cases, num_cubes, cube_block)

## Method 1:
# def can_stack_cubes(cubes):
#     d = deque(cubes)
#     print(d)
#     stack = [float('inf')]
#     # print(stack)

#     while d:
#         left, right = d[0], d[-1]
#         if right >= left and right <= stack[-1]:
#             # removes the rightmost cube from d and places it on top of the pile.
#             stack.append(d.pop())
#             print(stack)
#         # checks if the leftmost cube is smaller or equal to the top cube in the pile.
#         elif left <= stack[-1]:
#             stack.append(d.popleft())
#         else:
#             return "No"
#     return "Yes"

## Method 2:
def can_stack_cubes(cubes):
    while cubes:
        large=None
        # check if last element is greater than first.
        if cubes[-1] > cubes[0]:
            large = cubes.pop()
            print(f"Large pop: {large}")
        else:
            large = cubes.popleft()
            print(f"Large pop left: {large}")

        if len(cubes) == 0:
            return "Yes"
        
        if cubes[-1] > large or cubes[0] > large:
            return "No" 


num_test_cases = int(input())
for _ in range(num_test_cases):
    num_cubes = int(input())
    # cubes = list(map(int, input().split()))
    cubes = deque(map(int, input().split()))
    print(can_stack_cubes(cubes))











