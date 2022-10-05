def min_search(array):
    min_element = array[0]
    for i in range(1,len(array)):
        if min_element>array[i]:
            min_element = array[i]
    
    return min_element


array = [42,100,-3,6,0,1,2]
ans = min_search(array)
print(ans)