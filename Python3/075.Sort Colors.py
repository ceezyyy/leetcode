"""
@Title: 075. Sort Colors
@Tag: array / two pointers/ sort
@Date: Feb-19 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Solution one(two pass):


class Solution:
    def sortColors(self, N: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for n in N:
            if n == 0:
                r += 1
            if n == 1:
                w += 1
            if n == 2:
                b += 1
        for i, v in enumerate(N):
            if i < r:
                N[i] = 0
            if r <= i < r + w:
                N[i] = 1
            if i >= r+w:
                N[i] = 2
        return N


"""
Runtime: 28 ms, faster than 84.97% of Python3 online submissions for Sort Colors.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sort Colors.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)  
"""
