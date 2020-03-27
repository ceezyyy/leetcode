"""
@Title: 066. Plus One
@Tag: array
@Date: Mar-10 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Approach 1: (Naive)

class Solution:
    def plusOne(self, A: List[int]) -> List[int]:
        s, res = 0, []
        for a in A:
            s = s * 10 + a
        s += 1
        while s > 0:
            res.append(s % 10)
            s //= 10
        return res[::-1]


"""
Runtime: 32 ms, faster than 48.52% of Python3 online submissions for Plus One.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
