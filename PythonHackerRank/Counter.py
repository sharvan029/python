from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(Counter(myList))

x = int(input())
sizes = [int(x) for x in input().split()]
sizescounter = Counter(sizes)
ncust = int(input())
listpr = []
for i in range(1, ncust+1):
    size, price = map(int, input().split())
    if sizescounter[size] > 0:
        sizescounter[size] = sizescounter[size]-1
        listpr.append(price)
    else:
        continue
    # listpr.append(price)
tot = 0
for j in listpr:
    tot = tot+j
print(tot)
