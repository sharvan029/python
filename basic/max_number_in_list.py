# find max number in list
numberList = [15, 85, 35, 89, 125, 10, 1000, 1, 100, 20]
max_n = numberList[0]
for i in range(len(numberList)-1):
    if numberList[i] >= max_n:
        max_n = numberList[i]

print(max_n)
