"""
@Title: 168. Excel Sheet Column Title
@Tag: math / string
@Date: Feb-03 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n > 0:
            n -= 1  # 26 -> "Z"
            res += chr(n % 26 + ord('A'))
            n //= 26
        return res[::-1]


"""
Runtime: 20 ms, faster than 96.45% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
