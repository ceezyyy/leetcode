"""
@Title: 1260. Shift 2D Grid
@Tag: array
@Date: Feb-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0]),
        temp, res = [], [0] * (rows * cols)
        for i in range(rows):  # 2D -> 1D
            for j in range(cols):
                temp.append(grid[i][j])
        for i in range(len(res)):  # shifting
            res[(i + k) % (rows * cols)] = temp[i]
        for i in range(rows):  # 1D -> 2D
            for j in range(cols):
                grid[i][j] = res[i * cols + j]
        return grid


"""
Runtime: 184 ms, faster than 43.64% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
"""


"""
Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""
