from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
nlist = []
mlist = []
for i in range(n):
    nlist.append(input())
for j in range(m):
    mlist.append(input())
d['groupa'].append(nlist)
d['groupb'].append(mlist)

for b in d['groupb']:
    print(b)


