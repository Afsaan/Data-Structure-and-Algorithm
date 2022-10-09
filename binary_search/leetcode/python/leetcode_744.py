def ceiling(array, target):
    start_point = 0
    end_point = len(array)-1

    if target > array[end_point]:
        return array[start_point]
    while(start_point<=end_point):
        middle_point = (start_point + end_point)//2

        if array[middle_point] > target:
            end_point = middle_point-1
        elif array[middle_point] < target:
            start_point = middle_point+1
    return array[start_point%len(array)]

array = ["x","x","y","y"]
target = "z"

ans = ceiling(array, target)
print(ans)