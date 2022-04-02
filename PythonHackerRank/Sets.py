# print(set('Hameed'))
#find average of distinct elements in an array
arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
def average(array):
    nset = set(array)
    sums = 0
    for i in nset:
        sums = sums+i
    counts = len(nset)
    averages = sums/counts
    return averages

print(average(arr))

