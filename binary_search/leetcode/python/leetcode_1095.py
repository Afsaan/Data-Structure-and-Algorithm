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


def search_left(arr, peak_point, target):
    
    start_point = 0
    end_point = peak_point;

    while(start_point<=end_point):
        middle_point = (start_point + end_point) // 2

        if arr[middle_point] > target:
            end_point = middle_point-1
        elif arr[middle_point] < target:
            start_point = middle_point+1
        else:
            return middle_point
    
    return -1

def search_right(arr, peak_point, target):
    
    start_point = 0
    end_point = peak_point;

    while(start_point<=end_point):
        middle_point = (start_point + end_point) // 2

        if arr[middle_point] < target:
            end_point = middle_point-1
        elif arr[middle_point] > target:
            start_point = middle_point+1
        else:
            return middle_point
    
    return -1 


arr = [1,2,3,4,5,3,1]
target=5
start_point = peak_mountain(arr)

result = search_left(arr,start_point,target)
if result == -1:
    result = search_right(arr,start_point,target)

print(result)