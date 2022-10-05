def linear_search(array , target):
    for index in range(len(array)):
        if array[index] == target:
            return index

    return -1


array = [23,45,1,2,3,6,9,1,10]
target = 9
ans = linear_search(array,target)
print(ans)