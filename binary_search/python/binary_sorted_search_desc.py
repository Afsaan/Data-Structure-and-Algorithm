def binary_sorted_search(array, target):
    start_point = 0
    end_point = len(array)-1

    while(start_point<=end_point):
        middle_point = (start_point + end_point)//2

        if array[middle_point] > target:
            start_point = middle_point+1
        elif array[middle_point] < target:
            end_point = middle_point-1
        else:
            return middle_point
    return -1

array = [800,700,78,67,56,45,34,23,12,11]
target = 11

ans = binary_sorted_search(array, target)
print(ans)