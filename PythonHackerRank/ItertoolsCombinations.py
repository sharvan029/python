from itertools import combinations

s, k = input().split()
n = int(k)
sorteds = sorted(s)
for i in range(1, n+1):
    #print(str(i))
    comb = combinations(sorteds, i)
    for j in comb:
        out = ''.join(j)
        print(out)


