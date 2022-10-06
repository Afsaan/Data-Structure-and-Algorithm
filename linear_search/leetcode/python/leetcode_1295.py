# leetcode problem 1295

def even_digit(nums):
    count = 0
    for num in nums:
        if even(num):
            count +=1
    return count

def even(num):
    if num<0:
        num = num * -1
    return check_digits(num)
    
def check_digits(num):
    if len(str(num))%2 == 0:
        return True
    return False

nums = [12,345,0,6,-7896]
print(even_digit(nums))
