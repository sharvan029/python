from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
#print(list(product(a,b)))
res = product(a, b)
# output = ''
# for i in res:
#     output = output+str(i)+' '
# print(output)
print(*res)
