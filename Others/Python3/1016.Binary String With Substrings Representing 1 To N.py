"""
@Title: 1016. Binary String With Substrings Representing 1 To N
@Tag: str
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):  # from 1 to N
            sub = "{0:b}".format(i)  # int -> binary string
            if sub not in S:
                return False
        return True


"""
Runtime: 76 ms, faster than 8.28% of Python3 online submissions for Binary String With Substrings Representing 1 To N.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary String With Substrings Representing 1 To N.
"""
