"""
@Title: 415. Add Strings
@Tag: string 
@Date: Jan-28 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self.convert(num1) + self.convert(num2))

    def convert(self, num: str) -> int:
        res, i = 0, 0  # result, pointer
        while i < len(num):
            res = res * 10 + int(num[i])
            i += 1
        return res


"""
Runtime: 52 ms, faster than 29.51% of Python3 online submissions for Add Strings.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Add Strings.
"""
