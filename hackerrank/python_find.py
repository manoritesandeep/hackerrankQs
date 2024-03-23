sample_ls = [1, 2, 3, 5, 6, 8, 10, 'apple', 'blue']


def finder(val):
    if val in sample_ls:
        return 1
    else:
        return 0


for v in sample_ls:
    print(finder(v))


def finder(val):
    if isinstance(val, str) and val.find('apple') > -1:
        return 1
    else:
        return 0


for v in sample_ls:
    print(finder(str(v)))
