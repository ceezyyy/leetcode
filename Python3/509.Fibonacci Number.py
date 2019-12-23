"""
@Title: 509. Fibonacci Number
@Tag: dp
@Date: Dec-23 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def fib(self, N: int) -> int:
        # corner case
        if N == 0:
            return 0
        if N == 1:
            return 1
        dp = [0 for i in range(N+1)]  # memorization
        dp[0], dp[1] = 0, 1  # initialization
        for n in range(2, N+1):
            dp[n] = dp[n-1]+dp[n-2]
        return dp[n]


"""
Runtime: 20 ms, faster than 99.01% of Python3 online submissions for Fibonacci Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Fibonacci Number.
"""
