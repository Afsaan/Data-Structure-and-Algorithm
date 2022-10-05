from ctypes.wintypes import SMALL_RECT


def while_loop(array):
    start = 0
    while start < len(array):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]
        start +=1
    return array



def for_loop(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i+1, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        
        array[i] , array[smallest] = array[smallest] , array[i]
    
    return array

if __name__== '__main__':
    array = [64, 25, 12, 22, 11]
    res = for_loop(array)
    print(res)