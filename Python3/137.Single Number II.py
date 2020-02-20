"""
@Title: 137. Single Number II
@Tag: 
@Date: Feb-20 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def singleNumber(self, N: List[int]) -> int:
        N = sorted(N)
        if len(N) == 1:  # corner case
            return N[0]
        if N[0] != N[1]:  # front
            return N[0]
        if N[-2] != N[-1]:  # back
            return N[-1]
        for i in range(1, len(N)-1):  # mid
            if N[i] != N[i-1] and N[i] != N[i+1]:
                return N[i]


"""
Runtime: 52 ms, faster than 92.72% of Python3 online submissions for Single Number II.
Memory Usage: 14.4 MB, less than 73.33% of Python3 online submissions for Single Number II.
"""


"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
