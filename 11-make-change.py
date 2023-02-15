#
# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, 
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Example: 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#

def make_change_mem(coins, amount):
    memo = {}

    def min_coins(coins, amount):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        # since we need to consider the min len(coins) possibilities
        # we need a more complicated for-loop to create the aggregation section
        min_current = amount+1
        for i in range(len(coins)):
            if coins[i] == amount: 
                min_current = min(min_current, 1)
            if coins[i] > amount:
                # no solution with this coin, set min to amount+1 to 
                # represent no solution was possible. If any
                # other coin presents a solution, it's solution will always
                # be less than amount+1
                min_current = min(min_current, amount+1)
            if coins[i] < amount:
                ans = min_coins(coins, amount-coins[i])
                if ans > amount-coins[i]:
                    # no solution down the path if we use this coin, 
                    # set min to amount+1 
                    min_current = min(min_current, amount+1)
                else:
                    min_current = min(min_current, ans+1)
            
        memo[amount] = min_current
        return min_current
    ans = min_coins(coins, amount)
    if ans > amount:
        return -1
    else:
        return ans

def make_change_tab(coins, amount):
    # Set up our tabulation as array of length amount+1 initializing 
    # the value of each element to amount+1. Each element will represent
    # the min number of coins that can be used to achieve the amount
    # represented by the index. This means tab[0] is set to zero since 
    # it takes zero coins to achieve an amount of zero. 
    tab = [amount+1] * (amount+1)
    tab[0] = 0

    # Here's the trick, we are going to loop over every amount from 
    # 1 to amount and calculate the min coins that can be used to make
    # that amount. 
    for amt in range(1, amount+1):
        for c in coins:
            if amt - c >= 0: 
                # Logically this says, if subtracting the current coin
                # from the current 'amt' we are processing results in a value
                # that is greater than or equal to zero, then there could be 
                # a solution down this path, and the solution will be one more 
                # than the solution we have already determined at tab[amt-c]. 
                # If there as no solution at that smaller 'amt' (amt-c) then 
                # the value in tab[amt-c] will be target amount+1 or greater.
                tab[amt] = min(tab[amt], 1+tab[amt-c])

    if tab[amount] <= amount:
        return tab[amount]
    else: 
        return -1

coins = [1,3,5]
amount = 11
print(make_change_tab(coins, amount), ", ", make_change_mem(coins, amount))

coins = [1, 2, 3, 4, 5]
amount = 7
print(make_change_tab(coins, amount), ", ", make_change_mem(coins, amount))

coins = [4, 5]
amount = 11
print(make_change_tab(coins, amount), ", ", make_change_mem(coins, amount))
