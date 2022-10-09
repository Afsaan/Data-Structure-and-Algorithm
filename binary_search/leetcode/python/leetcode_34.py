def position(array, target, right_search):
    start_point = 0
    end_point = len(array)-1
    ans = -1
    while(start_point<=end_point):
        middle_point = (start_point + end_point)//2
        
        if array[middle_point] > target:
            end_point = middle_point-1
        elif array[middle_point] < target:
            start_point = middle_point+1
        else:
            # potential answer found
            ans = middle_point
            if right_search:
                end_point = middle_point - 1
            else:
                start_point = middle_point +1

    return ans

array = [5,7,7,8,8,10]
target = 10
final_array = [position(array, target, True), position(array, target, False)]
print(final_array)