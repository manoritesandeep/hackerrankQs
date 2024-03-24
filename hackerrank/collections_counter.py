"""
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

Task

is a shoe shop owner. His shop has number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay

amount of money only if they get the shoe of their desired size.

Your task is to compute how much money earned.

Input Format:
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N , the number of customers.
The next N lines contain the space separated values of the desired by the customer and, the price of the shoe.

Output Format:
Print the amount of money earned by Raghu

Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200

Explanation
Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.
Total money earned = 55 + 45 + 40 + 60=$200

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = 10
shoe_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
num_cust = 6
demand = [ {6 : 55}, {6 : 45}, {6 : 55}, {4 : 40}, {18 : 60}, {10 : 50} ]

# Supply
# Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})

# Demand
# Counter({6: 3, 4: 1, 18: 1, 10: 1})

shoe_size_count = Counter(shoe_sizes)
print(shoe_size_count)  # Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})

# demand_size_count = Counter(
#     [key for dict in demand for key in dict.keys()]
# )
# print(demand_size_count)

# prices = [value for dict in demand for value in dict.values()]
# print(prices)

total_sales = 0

for order in demand:
    for size, price in order.items():
        if shoe_size_count[size] > 0:
            total_sales += price
            shoe_size_count[size] -= 1
print(total_sales)


