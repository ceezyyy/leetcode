"""
@Title: 007. Reverse Integer
@Tag: str
@Date: Jan-03 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def reverse(self, x: int) -> int:
        k = str(x)  # int -> str
        if k[0] == '-':  # negative number
            k = k[1:]  # get rid of the '-' first
            return -(int(k[::-1])) if -(int(k[::-1])) > -2**31 else 0
        else:  # positive number
            return int(k[::-1]) if int(k[::-1]) < 2**31-1 else 0


"""
within the 32-bit signed integer range: [−231,  231 − 1]
"""


"""
Runtime: 20 ms, faster than 98.66% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
"""
