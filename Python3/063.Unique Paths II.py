"""
@Title: 063. Unique Paths II
@Tag: dp
@Date: Dec-16 2019
@Author: ceezyyy
@Difficulty: Medium
@Reference: @fuxuemingzhu  https://github.com/fuxuemingzhu
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for i in range(rows)]  # memory (two-dimension)
        # corner case e.g: [[1]]
        if obstacleGrid[0][0] == 1:
            return 0
        # initialization (a bit different from "Unique Path")
        dp[0][0] = 1
        for i in range(rows):  # for loop
            for j in range(cols):
                if obstacleGrid[i][j] == 0:  # empty
                    if i != 0:  # the first row without "top"
                        dp[i][j] += dp[i-1][j]
                    if j != 0:  # the first col without "left"
                        dp[i][j] += dp[i][j-1]
        return dp[rows-1][cols-1]


"""
Runtime: 44 ms, faster than 89.98% of Python3 online submissions for Unique Paths II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Paths II.
"""
