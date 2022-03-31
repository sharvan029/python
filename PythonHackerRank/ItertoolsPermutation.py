from itertools import permutations
# print(list(permutations([1,2,3])))
# print(list(permutations([1,2,3], 2)))

s, k = input().split()
per = sorted(list(permutations(s, int(k))))

for item in per:

    out = ''.join(item)
    print(out)
