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


arr = [3,4,5,1]
peak_mountain(arr)