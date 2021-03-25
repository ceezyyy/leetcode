"""
@Title: 064. Minimum Path Sum
@Tag: dp
@Date: Dec-22 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # bottom-up approach
        rows, cols = len(grid), len(grid[0])
        # corner case
        if rows*cols == 1:
            return grid[0][0]
        # memorization: dp[i] stands for the min current path (one-dimension dp[])
        dp = [0 for i in range(rows*cols)]
        dp[0] = grid[0][0]  # initialization
        for i in range(1, rows*cols):  # 1-D array is magical
            if i < cols:  # the first row
                dp[i] += dp[i-1]+grid[0][i % cols]
            elif i % cols == 0:  # the first col
                dp[i] += dp[i-cols]+grid[i//cols][i % cols]
            else:  # others
                dp[i] = min(dp[i-1], dp[i-cols])+grid[i//cols][i % cols]
        # print(dp)
        return dp[i]  # bottom-right


"""
Runtime: 112 ms, faster than 60.52% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15 MB, less than 26.32% of Python3 online submissions for Minimum Path Sum.
"""
