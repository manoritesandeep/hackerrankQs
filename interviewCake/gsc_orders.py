"""
In order to win the prize for most cookies sold, 
my friend Alice and I are going to merge our Girl Scout Cookies orders 
    and enter as one unit. 

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))

Write a function to merge our lists of orders into one sorted list. 
"""

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# my_list.extend(alices_list)
# sorted_list = sorted(my_list)
# print(sorted_list)

final_list = sorted(my_list + alices_list)
print(f"Final list: {final_list}")

## Solution
"""
To merge two sorted lists into one sorted list, you can use a two-pointer technique. 

Start at the beginning of each list, and always choose the smaller of the two current elements
    to add to the result list. 
Move the pointer forward in the list from which you took the smaller element, 
    and repeat until you've exhausted both lists.
"""
def merge_lists(list1, list2):
    merged_list = []
    i = j = 0

    # Merge elements from list1 and list2 until one list is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If list1 is not exhausted, add remaining elements to merged_list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If list2 is not exhausted, add remaining elements to merged_list
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_lists(my_list, alices_list))  # Outputs: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]