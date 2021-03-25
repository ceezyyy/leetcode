"""
@Title: 118. Pascal's Triangle
@Tag: dp
@Date: Dec-31 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # memorization (set default as one)
        dp = [[1 for j in range(i+1)] for i in range(numRows)]
        for row in range(2, numRows):  # start from the row[2]
            for col in range(1, row):
                dp[row][col] = dp[row-1][col-1]+dp[row-1][col]
        return dp


"""
Runtime: 28 ms, faster than 81.27% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
"""


"""
Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""
