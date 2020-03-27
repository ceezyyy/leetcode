"""
@Title: 1380. Lucky Numbers in a Matrix
@Tag: array
@Date: Mar-20 2020
@Author: ceezyyy
@Difficulty: Easy
"""

# Approach 1: (Brute Force)


class Solution:
    def luckyNumbers(self, A: List[List[int]]) -> List[int]:
        rows, cols, row_min, col_max = len(A), len(A[0]), [], []
        for i in range(rows):  # the min of the rows
            row_min.append(min(A[i]))
        for j in range(cols):  # the max of the cols
            temp = 0
            for i in range(rows):
                temp = A[i][j] if A[i][j] > temp else temp
            col_max.append(temp)
        return [x for x in row_min if x in col_max]


# Approach 2: (Optimized Brute Force)


class Solution:
    def luckyNumbers(self, A: List[List[int]]) -> List[int]:
        rows, cols = len(A), len(A[0])
        row_min, col_max = [float("inf")] * rows, [0] * cols
        for i in range(rows):
            for j in range(cols):
                row_min[i] = A[i][j] if A[i][j] < row_min[i] else row_min[i]
                col_max[j] = A[i][j] if A[i][j] > col_max[j] else col_max[j]
        return [x for x in row_min if x in col_max]


"""
Time Complexity: O(mn)
Space Complexity: O(1)
"""
