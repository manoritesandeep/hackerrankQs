"""
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, 
    worried it's a plot to break into a major European National Cake Vault. 
    The message has been mostly deciphered, but all the words are backward! 
    Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters 
    and reverses the order of the words in place. 

 For example:

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

"""

## try
# def reverse_words(word_message):
#     left_idx = 0
#     right_idx = len(word_message) - 1

#     while left_idx < right_idx:
#         word_message[left_idx], word_message[right_idx] = \
#             word_message[right_idx], word_message[left_idx]

#     return word_message.reverse()

# message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
# print(''.join(message))   # cake pound steal

# word_msg = list(''.join(message))
# print(f"word message: {word_msg} of class type {type(word_msg)}")
# print(f"The reverse message is: {reverse_words(word_msg)}")


## try 2 - method 2
# message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]

# message_str = "".join(message)
# print(f"Message string: {message_str}")

# words = message_str.split(" ")
# print(f"Words are: {words}")

# words.reverse()
# print(f"words :{words}")

# reversed_message = " ".join(words)
# print(f"Reversed message: {reversed_message}") # Reversed message: steal pound cake

def reversed_message(message):
    message_str = "".join(message)

    # split words
    words = message_str.split(" ")

    # reverse
    words.reverse()

    # add split words to sentence
    reversed_msg = " ".join(words)

    return reversed_msg

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

print(f"Reversed message is:\n{reversed_message(message=message)}")

## Solution
# def reverse_words(message):
#     # First we reverse all the characters in the entire message
#     reverse_characters(message, 0, len(message)-1)

#     # This gives us the right word order
#     # but with each word backward

#     # Now we'll make the words forward again
#     # by reversing each word's characters

#     # We hold the index of the *start* of the current word
#     # as we look for the *end* of the current word
#     current_word_start_index = 0

#     for i in range(len(message) + 1):
#         # Found the end of the current word!
#         if (i == len(message)) or (message[i] == ' '):
#             reverse_characters(message, current_word_start_index, i - 1)
#             # If we haven't exhausted the message our
#             # next word's start is one character ahead
#             current_word_start_index = i + 1


# def reverse_characters(message, left_index, right_index):
#     # Walk towards the middle, from both sides
#     while left_index < right_index:
#         # Swap the left char and right char
#         message[left_index], message[right_index] = \
#             message[right_index], message[left_index]
#         left_index  += 1
#         right_index -= 1

### Verdict:
"""
Both solutions have the same time complexity of O(n), 
    where n is the length of the message. 
    However, the second solution (Solution 2) is more 
    space-efficient than the first one (Solution 1).

Solution 1 creates a new string and a new list of words, 
    which requires additional space. It first joins the 
    characters into a string, splits the string into words, 
    reverses the list of words, and then joins the words back
    into a string. Each of these operations creates a new object.

Solution 2, on the other hand, performs all operations in-place, 
    without creating any new strings or lists. 
    It first reverses all characters in the message, 
    and then reverses the characters in each word. 
    Both of these operations are done directly on the input list,
    so they don't require any additional space.

Therefore, if memory usage is a concern, Solution 2 would be the better choice. 
    However, if the input message is not too large, 
    both solutions should work fine in practice.
"""