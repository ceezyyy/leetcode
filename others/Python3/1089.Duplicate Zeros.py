"""
@Title: 1089. Duplicate Zeros
@Tag: array
@Date: Feb-05 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def duplicateZeros(self, A: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if A.count(0) == 0:
            return
        B, n = [], len(A)
        for a in A:
            B.append(a)
            if a == 0:
                B.append(0)
        A[:] = B[:n]  # replace


"""
Runtime: 68 ms, faster than 82.00% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
