"""
Write a function that takes a list of characters and reverses the letters in place.

"""

def reverse_char(lst):
    left_index=0
    right_index=len(lst) - 1

    while left_index < right_index:
        # swap characters 
        lst[left_index], lst[right_index] = lst[right_index], lst[left_index]

        # move towards middle
        left_index += 1
        right_index -= 1

    return lst 

# usage
# sample_str = ["aab", "def", "bac", "cap", "faq"]
sample_str = ['aaa', 'bbb', 'ccc']
reverse_char(sample_str)

