"""
@Title: 074. Search a 2D Matrix
@Tag: binary search
@Date: Jan-13 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:  # corner case
            return False
        n = len(matrix[0])  # cols
        left = 0  # left pointer
        right = len(matrix) * len(matrix[0]) - 1  # right pointer
        while left <= right:  # binary search: 2D array -> 1D array
            mid = left + (right - left) // 2
            if target == matrix[mid // n][mid % n]:
                return True
            elif target < matrix[mid // n][mid % n]:
                right = mid - 1
            else:  # target > matrix[mid//n][mid%n]
                left = mid + 1
        return False  # not found


"""
Runtime: 64 ms, faster than 77.82% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
"""


"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""
