"""
@Title: 059. Spiral Matrix II
@Tag: array / simulation
@Date: Feb-29 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0 for j in range(n)] for i in range(n)]  # square
        left, right, top, bottom, k = 0, n, 0, n, 1
        while k <= n ** 2:
            for j in range(left, right):
                if k > n ** 2:
                    return M
                M[top][j] = k
                k += 1
            top += 1
            for i in range(top, bottom):
                if k > n ** 2:
                    return M
                M[i][right-1] = k
                k += 1
            right -= 1
            for j in range(right-1, left-1, -1):
                if k > n ** 2:
                    return M
                M[bottom-1][j] = k
                k += 1
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                if k > n ** 2:
                    return M
                M[i][left] = k
                k += 1
            left += 1
        return M


"""
Runtime: 32 ms, faster than 43.91% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.
"""


"""
Time Complexity: O(n), n is the total elements of the matrix
Space Complexity: O(1), res is not regraded as extra space
"""
