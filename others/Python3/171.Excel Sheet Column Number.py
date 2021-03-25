"""
@Title: 171. Excel Sheet Column Number
@Tag: math / bit
@Date: Jan-21 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        length, res = len(s), 0
        for ch in s:
            length -= 1
            res += (ord(ch) - ord('A') + 1) * 26 ** length  # 26-based
        return res


"""
Runtime: 28 ms, faster than 79.39% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
