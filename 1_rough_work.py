# def sum1(n):
#     total = 0
#     for i in n:
#         print(i)
#         total += i
#
#     return total
#
#
# print(sum1([1000, 2000, 3000, 4000, 5000]))

##############################################

mat = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
len_mat = len(mat)
# print(len_mat)    #3
print(mat[0][0])
# print(mat[0][len_mat-1])
print(mat[1][int(len_mat/2)])
print(mat[2][len_mat-1])
l2r = mat[0][0] + mat[1][int(len_mat/2)] + mat[2][len_mat-1]
r2l = mat[0][len_mat-1] + mat[1][int(len_mat/2)] + mat[2][0]
print(l2r)
print(r2l)
print(abs(l2r-r2l))
