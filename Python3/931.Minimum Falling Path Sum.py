"""
@Title: 931. Minimum Falling Path Sum
@Tag: dp
@Date: Dec-30 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        # corner case
        if len(A) == 1:  # square array
            return A[0][0]
        rows = len(A)
        cols = len(A[0])
        # the min falling path sum
        dp = [[0 for col in range(cols)] for row in range(rows)]
        # a falling path starts at any element in the first row
        for col in range(cols):  # the first row
            dp[0][col] = A[0][col]
        for row in range(1, rows):  # start from the second row
            for col in range(cols):  # scan every col
                if col == 0:  # the first col
                    dp[row][col] = min(
                        dp[row-1][col], dp[row-1][col+1])+A[row][col]
                elif col == cols-1:  # the last col
                    dp[row][col] = min(
                        dp[row-1][col], dp[row-1][col-1])+A[row][col]
                else:
                    dp[row][col] = min(
                        dp[row-1][col-1], dp[row-1][col], dp[row-1][col+1])+A[row][col]
        return min(dp[-1])


"""
Runtime: 124 ms, faster than 74.94% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Minimum Falling Path Sum.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
