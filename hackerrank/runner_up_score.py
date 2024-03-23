"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given n scores. 
Store them in a list and find the score of the runner-up.
"""

# Method 1:
if __name__ =='__main__':
    # n = int(input())
    n = [2,3,6,6,5]
    # arr = map(int, n)
    # print(arr)
    
    print(sorted(set(n), reverse=True)[1])
    # print(sorted(set(n), reverse=False)[-2])

# Method 2:
# if __name__ =='__main__':
#     n = [3,4,4,5,6,7,8,9,9]
#     max_num = max(n)
#     print(f"Max number: {max_num}")
#     sc = None

#     for num in n:
#         if num == max_num:
#             pass
#         elif sc == None:
#             sc = num
#             print(f"Elif1: {sc}")
#         elif num > sc:
#             sc = num
#             print(f"Elif2: {sc}")
#     print(sc)

