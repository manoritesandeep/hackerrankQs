from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")

for i in d.items():
    print(i)


# n, m = map(int, input().split())
# group_A = [input() for _ in range(n)]
# group_B = [input() for _ in range(m)]
    
n, m = 5, 2
group_A = ['a', 'a', 'b', 'a', 'b']
group_B = ['a', 'b']

d = defaultdict(list)

for index, word in enumerate(group_A, start=1):
    d[word].append(index)

print(d)

for word in group_B:
    if word in d:
        print(' '.join(map(str, d[word])))
    else:
        print(-1)