"""
@Topic: 1137. N-th Tribonacci Number
@Tag: dp
@Date: Dec-14 2019
@Author: ceezyyy
@Difficulty: Easy 
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # corner case
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        res = [0]*(n+1)  # memory dp
        res[0] = 0  # T0 = 0
        res[1] = 1  # T1 = 1
        res[2] = 1  # T2 = 1
        for i in range(3, n+1):
            res[i] = res[i-3]+res[i-2]+res[i-1]
        return res[n]


"""
Runtime: 24 ms, faster than 94.36% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for N-th Tribonacci Number.
"""
