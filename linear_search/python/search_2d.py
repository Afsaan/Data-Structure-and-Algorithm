def search_2d(array, target):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == target:
                return [i,j]

    return -1


array = [
    [10,24,54],
    [11,78,72],
    [5,8,45]
]

target = 24

print(search_2d(array,target))
