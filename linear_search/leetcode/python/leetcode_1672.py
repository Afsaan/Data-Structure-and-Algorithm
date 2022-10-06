
def max_wealth(accounts):
    max_wealth = 0
    
    for bank in accounts:
        wealth = 0
        for money in bank:
            wealth = wealth + money
        if max_wealth < wealth:
            max_wealth  = wealth
    
    return max_wealth



accounts = [[1,2,3],[3,2,1]]
print(max_wealth(accounts))