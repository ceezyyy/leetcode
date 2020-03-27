"""
@Title: 931. Minimum Falling Path Sum
@Tag: dp
@Date: Dec-30 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows = len(A)  # maybe it's easy to understand
        cols = len(A[0])
        # no extra space, but it's not a good way to change the original input in the real world
        for row in range(1, rows):  # start from the second row
            for col in range(cols):
                topleft = A[row-1][col-1] if col != 0 else float('inf')
                topright = A[row-1][col+1] if col != cols-1 else float('inf')
                A[row][col] += min(topleft, topright, A[row-1][col])
        return min(A[-1])


"""
Runtime: 116 ms, faster than 91.10% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 13.6 MB, less than 50.00% of Python3 online submissions for Minimum Falling Path Sum.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(1）
"""
