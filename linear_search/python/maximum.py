def max_search(array):
    max_element = array[0]
    for i in range(1,len(array)):
        if max_element<array[i]:
            max_element = array[i]
    
    return max_element


array = [42,100,-3,6,0,1,2]
ans = max_search(array)
print(ans)