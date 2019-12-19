"""
@Title: 120. Triangle
@Tag: dp
@Date: Dec-19 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # corner case
        if len(triangle) == 1:
            return triangle[0][0]
        # memory(The array is 2-dimension)
        dp = [[0]*i for i in range(1, len(triangle)+1)]
        dp[0][0] = triangle[0][0]  # initialization
        for row in range(1, len(triangle)):  # for loop
            for col in range(len(dp[row])):
                # three situations
                if col == 0:  # the first col  -- situation 1
                    dp[row][0] = dp[row-1][col]+triangle[row][col]
                elif col == len(dp[row])-1:  # the last col  -- situation 2
                    dp[row][col] = dp[row-1][col-1]+triangle[row][col]
                else:  # situation 3
                    dp[row][col] = min(
                        dp[row-1][col-1], dp[row-1][col])+triangle[row][col]
        return min(dp[-1])


"""
Runtime: 56 ms, faster than 94.28% of Python3 online submissions for Triangle.
Memory Usage: 13.6 MB, less than 33.33% of Python3 online submissions for Triangle.
"""
