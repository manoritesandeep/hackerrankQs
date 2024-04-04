"""

"""

from itertools import combinations
import sys
import io


def calc_prob(n, letters, k):
    """
    Input:
    n - length of list
    letters - the elements in the list
    k - denoting the number of indices to be selected.

    Output: 
    Single line consisting of the probability that at least one of the K 
        indices selected contains the letter:'a'.
    """
    # generate all combinations
    comb = list(combinations(letters, k))

    # Find combinations where 'a' is present
    comb_a = [c for c in comb if 'a' in c]

    # calculate probability
    prob = len(comb_a) / len(comb)

    return round(prob, 3)

# use the function
sample_input = """4 
a a c d
2
"""

# Redirect standard input to read from sample_input
sys.stdin = io.StringIO(sample_input)

print(
    calc_prob(
        n=int(input()),
        letters=input().split(),
        k=int(input())
    )
)


