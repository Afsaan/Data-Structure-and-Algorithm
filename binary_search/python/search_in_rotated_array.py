def pivot_index(array):
    start = 0
    end = len(array) - 1

    if len(array) == 1:
        return start

    while start<=end:
        middle = (start + end) // 2

        if array[middle] > array[middle+1]:
            return middle
        elif array[middle] < array[middle-1]:
            return middle-1
        elif array[start] >= array[middle]:
            end = middle-1
        else:
            start = middle + 1

    return -1


nums = [3,1]
target = 1

pivot = pivot_index(nums)
print(pivot)


