def count_frequency(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] =1
    return freq

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)