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

def make_change(coins, amount):
    return 0

coins = [1,3,5]
amount = 11
print(make_change(coins, amount))

coins = [1, 2, 3, 4, 5]
amount = 7
print(make_change(coins, amount))

coins = [4, 5]
amount = 11
print(make_change(coins, amount))
