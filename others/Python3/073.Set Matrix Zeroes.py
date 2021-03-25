"""
@Title: 073. Set Matrix Zeroes
@Tag: array
@Date: Feb-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def setZeroes(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols, first_row, first_col = len(M), len(M[0]), False, False
        # step one: use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.
        for j in range(cols):  # check the first row
            if M[0][j] == 0:
                first_row = True
        for i in range(rows):  # walk through
            if M[i][0] == 0:
                first_col = True  # check the first col
            for j in range(cols):
                if M[i][j] == 0:
                    M[i][0] = 0  # flag
                    M[0][j] = 0
        # step two: set zeros
        for i in range(1, rows):  # walk through but start the index from one
            for j in range(1, cols):
                if not M[i][0] or not M[0][j]:  # either
                    M[i][j] = 0
        # step three: check the flag
        if first_row:
            for j in range(cols):
                M[0][j] = 0
        if first_col:
            for i in range(rows):
                M[i][0] = 0


"""
Runtime: 140 ms, faster than 51.21% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 13.4 MB, less than 97.44% of Python3 online submissions for Set Matrix Zeroes.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
