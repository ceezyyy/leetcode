"""
@Topic: 062. Unique Paths
@Tag: dp
@Date: Dec-15 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*(m*n)  # memory
        dp[0] = 1  # only one grid
        for i in range(1, n*m):
            if i < n:  # the first row without "top"
                dp[i] = dp[i-1]
            elif (i % n == 0):  # the first col without "left"
                dp[i] = dp[i-n]
            else:
                dp[i] = dp[i-1]+dp[i-n]  # recursion
        return dp[m*n-1]  # the bottom-right


"""
Runtime: 20 ms, faster than 99.18% of Python3 online submissions for Unique Paths.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Paths.
"""
