"""
@Title: 1362. Closest Divisors
@Tag: math
@Date: Feb-23 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        k1, k2, res, res1, res2 = num + 1, num + 2, [], [], []
        for i in range(1, int(math.sqrt(k1)) + 1):  # factors of num + 1
            if k1 % i == 0:
                res1.append(i)
        for j in range(1, int(math.sqrt(k2)) + 1):  # factors of num + 2
            if k2 % j == 0:
                res2.append(j)
        if not res1:
            return [res2[-1], k2 // res2[-1]]
        if not res2:
            return [res1[-1], k1 // res1[-1]]
        return [res1[-1], k1 // res1[-1]] if res1[-1] >= res2[-1] else [res2[-1], k2 // res2[-1]]


"""
Runtime: 264 ms, faster than 100.00% of Python3 online submissions for Closest Divisors.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Closest Divisors.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
