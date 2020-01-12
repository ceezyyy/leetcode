"""
@Title: 1281. Subtract the Product and Sum of Digits of an Integer
@Tag: 
@Date: Jan-12 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = []
        while n > 0:
            res.append(n % 10)
            n //= 10
        # math.prod() is available in Python 3.8
        return math.prod(res) - sum(res)


"""
Runtime: 24 ms, faster than 83.24% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""
