def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(0, len(array)):
        for j in range(i+1, len(array)): 
            if array[i]+array[j] == targetSum:
                return [i,j]
    
    return []

print(twoNumberSum([2,7,11,15] , 9))
print(twoNumberSum([3,2,4] , 6))
print(twoNumberSum([3,3] , 6))