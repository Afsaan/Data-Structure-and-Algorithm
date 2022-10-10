def find_order(array):
    start = 0
    end = len(array)-1

    if array[start] < array[end]:
        return True
    return False


def order_agnostic_search(array,target):
    start = 0
    end = len(array)-1

    is_asc = find_order(array)

    while(start<=end):

        middle = (start + end) // 2

        if array[middle] == target:
            return middle

        if is_asc:
            if array[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        else:
            if array[middle] > target:
                start = middle + 1
            else:
                end = middle - 1
    return -1

array_test = [10,20,30,40,50,67,68,69,100]
array_test_2 = [98,96,65,54,43,32,21]
target = 54

    
ans = order_agnostic_search(array_test, target)
print(ans)