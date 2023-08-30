import numpy as np

ls = [6.5,3.6,2.5,10.1,7.3]

std = np.std(ls)
print(std)

mean = np.mean(ls)
print(f"mean is: {mean}")

median = np.median(ls)
print(f"median is: {median}")

# common element
lst = [1,1,2,2,3,4,5,6,7,2,2,1,1,1,1,2,2,44,5,2]
most_common = max(set(lst), key=lst.count)
print(f"most common element: {most_common}")

# string to int
str_lst = ['1','2','3']
int_lst = list(map(int,str_lst))
print(f"String to Integers: {int_lst}")