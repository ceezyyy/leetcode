"""
@Title: 344. Reverse String
@Tag: str
@Date: Jan-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  # in-place


"""
Runtime: 204 ms, faster than 93.45% of Python3 online submissions for Reverse String.
Memory Usage: 17.3 MB, less than 95.35% of Python3 online submissions for Reverse String.
"""
