"""
@Title: 788. Rotated Digits
@Tag: string 
@Date: Jan-29 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for n in range(1, N + 1):  # from 1 to N are good
            if self.isGoodNum(n):
                res += 1
        return res

    def isGoodNum(self, N: int) -> bool:
        good, bad, valid = [2, 5, 6, 9], [3, 4, 7], False
        while N:
            if N % 10 in bad:  # each digit must be rotated - we cannot choose to leave it alone
                return False
            if N % 10 in good:  # at least one which can be rotated and different from previous
                valid = True
            N //= 10
        return valid


"""
Runtime: 96 ms, faster than 57.78% of Python3 online submissions for Rotated Digits.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Rotated Digits.
"""
