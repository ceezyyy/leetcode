"""
@Title: 1342. Number of Steps to Reduce a Number to Zero
@Tag: bit manipulation
@Date: Feb-09 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            res += 1
        return res


"""
Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
"""
