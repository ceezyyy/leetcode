"""
@Title: 1351. Count Negative Numbers in a Sorted Matrix
@Tag: array
@Date: Feb-16 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def countNegatives(self, G: List[List[int]]) -> int:
        row, col, res = len(G), len(G[0]), 0
        for i in range(row):
            for j in range(col):
                if G[i][j] < 0:
                    res += 1
        return res


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
