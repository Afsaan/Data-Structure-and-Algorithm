"""arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 """




def while_loop(array):
    start = 0
    while start < len(array):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]
        start +=1
    return array



def for_loop(array):
    for _ in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]

    return array

if __name__== '__main__':
    array = [64, 25, 12, 22, 11]
    res = while_loop(array)
    print(res)