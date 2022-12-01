def ceiling(array, target):
    start_point = 0
    end_point = len(array)-1

    while start_point <= end_point:
        middle_point = (start_point + end_point)//2

        if target > array[middle_point]: 
            start_point = middle_point + 1
        else:
            end_point = middle_point - 1
            

    if start_point == len(array):
        return array[0]
    else:
        return array[start_point]
        

array = ["c","f","j","y"]
target = "d"

ans = ceiling(array, target)
print(ans)