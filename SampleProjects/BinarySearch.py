import time

l = []


def generate_list(n):
    for item in range(n):
        l.append(item)
    return l


# Check item using for loop
def check_element(elm):
    start_time = time.time_ns()
    for item in l:
        if item == elm:
            return item
    end_time = time.time_ns()
    time_duration = end_time - start_time
    print(time_duration)
    return -1


# check using binary search
def binary_search(elm, l):
    while len(l) > 0:
        midelement = len(l)//2
        if l[midelement] == elm:
            return l[midelement]
        elif l[midelement] > elm:
            l = l[0: midelement]
        else:
            l = l[midelement+1:len(l)]
    print(time_duration)
    return -1


list = generate_list(1000)
print(check_element(900))
print(binary_search(910, list))
