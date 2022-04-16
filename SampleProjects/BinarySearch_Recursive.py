# BinarySearch using using loop
def binary_search_loop(array, x, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result_loop = binary_search_loop(array, x, 0, len(array)-1)

if result_loop != -1:
    print("Element is present at index " + str(result_loop))
else:
    print("Not found")


# BinarySearch using recursive
def binary_search_recursive(array, x, low, high):
        mid = low + (high-low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
            binary_search_recursive(array, x, low, high)
        else:
            high = mid - 1
            binary_search_recursive(array, x, low, high)
        return -1


x = 2
result_recursive = binary_search_loop(array, x, 0, len(array)-1)

if result_recursive != -1:
    print("Element is present at index " + str(result_recursive))
else:
    print("Not found")


