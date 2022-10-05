def search_range(array, range_value, target):
    for index in range(range_value[0], range_value[1]+1):
        if array[index] == target:
            return index
    
    return -1


array = [1,2,4,6,33,4,5]
range_value = [1,5]
target = 4

ans = search_range(array, range_value, target)
print(ans)