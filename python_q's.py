#Find the output of the following program:
L1 = []
L1.append([1, [2, 3], 4])
# print(L1)
# print(type(L1))
L1.extend([7, 8, 9])
print(L1)   # [[1, [2, 3], 4], 7, 8, 9]
# print(type(L1))
print(L1[0])    # [1, [2, 3], 4]
print(L1[0][1]) # [2, 3]
print(L1[0][1][1])  # 3
print(L1[2])    # 8
print(L1[0][1][1] + L1[2])  # 3 + 8 = 11