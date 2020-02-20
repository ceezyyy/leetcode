"""
@Title: 136. Single Number
@Tag: 
@Date: Feb-20 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def singleNumber(self, N: List[int]) -> int:
        N, n = sorted(N), len(N)
        if n == 1:  # corner case
            return N[0]
        if N[0] != N[1]:  # front
            return N[0]
        if N[-1] != N[-2]:  # back
            return N[-1]
        for i in range(1, n-1):  # mid
            if N[i] != N[i-1] and N[i] != N[i+1]:
                return N[i]


"""
Runtime: 88 ms, faster than 67.33% of Python3 online submissions for Single Number.
Memory Usage: 15.2 MB, less than 8.20% of Python3 online submissions for Single Number.
"""


"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
