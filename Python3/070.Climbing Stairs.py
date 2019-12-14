"""
@Topic: 070. Climbing Stairs
@Tag: dp
@Date: Dec-14 2019
@Author: ceezyyy
@Difficulty: Easy 
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # corner case
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*(n+1)  # memory
        # exit
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]  # recursion
        return dp[i]


"""
Runtime: 24 ms, faster than 94.38% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
"""
