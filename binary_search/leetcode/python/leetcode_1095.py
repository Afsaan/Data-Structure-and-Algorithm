def peak_mountain(arr):
    start_point = 0
    end_point = len(arr)-1

    while(start_point<end_point):
        middle_point = (start_point + end_point) // 2
        if arr[middle_point] > arr[middle_point+1]:
            end_point = middle_point
        elif arr[middle_point] < arr[middle_point+1]:
            start_point = middle_point+1

    return start_point


def order(array,start_point,end_point):
    if array[start_point] > array[end_point]:
        return True
    return False


def order_agnostic(array, target , start_point , end_point):

    is_asc = order(array,start_point,end_point)

    while(start_point<=end_point):
        middle = (start_point + end_point) // 2

        if array[middle] == target:
            return middle

        if is_asc:
            if array[middle] > target:
                end_point = middle - 1
            else:
                start_point = middle + 1
        else:
            if array[middle] < target:
                end_point = middle - 1
            else:
                start_point = middle + 1

    return -1


arr = [1,2,4,5,3,1]
target=3
point = peak_mountain(arr)
print(point)

result = order_agnostic(arr, target, start_point = 0, end_point = point)
if result == -1:
    result = order_agnostic(arr, target, start_point=point, end_point=len(arr)-1)

print(result)