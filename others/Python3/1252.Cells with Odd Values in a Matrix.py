"""
@Title: 1252. Cells with Odd Values in a Matrix
@Tag: array
@Date: Jan-31 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols, res = [0] * n, [0] * m, 0  # initialization
        for i, j in indices:
            rows[i], cols[j] = rows[i] ^ 1, cols[j] ^ 1  # 0 -> even, 1 -> odd
        for i in range(n):
            for j in range(m):
                res += 1 if rows[i] ^ cols[j] == 1 else 0
        return res


"""
Runtime: 60 ms, faster than 26.87% of Python3 online submissions for Cells with Odd Values in a Matrix.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
