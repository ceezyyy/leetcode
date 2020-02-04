"""
@Title: 1317. Convert Integer to the Sum of Two No-Zero Integers
@Tag: math
@Date: Feb-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):  # loop through all elements from 1 to n
            if self.check(i) and self.check(n - i):
                return [i, n - i]

    def check(self, n: int) -> bool:  # check if n is No-Zero integer
        while n > 0:
            if n % 10 == 0:
                return False
            n //= 10
        return True


"""
Runtime: 40 ms, faster than 9.04% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
"""
