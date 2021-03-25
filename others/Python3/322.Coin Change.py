"""
@Title: 322. Coin Change
@Tag: dp
@Date: Dec-22 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    # dp: bottom-up approach
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize dp as all the value is invalid (amount+1)
        # zero-based since we need "amount+1"
        dp = [amount+1 for i in range(amount+1)]  # memorization table
        # when the "amount" is  zero, the number of coins to make it up is zero as well
        dp[0] = 0
        for coin in coins:  # for loop each coin firstly
            # start from the dp[current_coin], which is an ingenious approach
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)  # update(the min)
        return dp[-1] if dp[-1] != amount+1 else -1


"""
Runtime: 1308 ms, faster than 65.84% of Python3 online submissions for Coin Change.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Coin Change.
"""


"""
Complexity Analysis:
Time complexity : O(S*n)
Space complexity : O(S). We use extra space for the memorization table.
"""
