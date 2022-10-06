def search_2d_min(array):
    min_value = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < min_value:
                min_value = array[i][j]

    return min_value


array = [
    [10,24,54],
    [11,78,72],
    [5,8,45]
]

print(search_2d_min(array))