def ceiling(array, target):
    start_point = 0
    end_point = len(array)

    while(start_point<=end_point):
        middle_point = (start_point + end_point)//2

        if array[middle_point] > target:
            end_point = middle_point-1
        elif array[middle_point] < target:
            start_point = middle_point+1
        else:
            return middle_point
    return start_point

array = [-10,-7,-2,10,45,78,100,200,600,800]
target = 812

ans = ceiling(array, target)
print(ans)