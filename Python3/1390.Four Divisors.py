"""
@Title: 1390. Four Divisors
@Tag: math
@Date: Mar-22 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            temp = []
            for i in range(1, int(math.sqrt(n)) + 1):  # find all the divisors
                if n % i == 0:
                    temp.extend([i, n // i])
                if len(temp) > 4:  # accelerate the process
                    break
            if len(temp) == 4 and len(temp) == len(set(temp)):  # check whether unique divisors
                res += sum(temp)
        return res


"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
