"""
@Title: 136. Single Number
@Tag: 
@Date: Feb-20 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Solution 1: (Sort & One Pass)


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


# Solution 2: (Hashset & One pass)


class Solution:
    def singleNumber(self, N: List[int]) -> int:
        s = set()
        for n in N:
            if n not in s:
                s.add(n)
            else:
                s.remove(n)
        return s.pop()


"""
Runtime: 84 ms, faster than 85.75% of Python3 online submissions for Single Number.
Memory Usage: 15 MB, less than 21.31% of Python3 online submissions for Single Number.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


# Approach 3: (Bit Manipulation)


class Solution:
    def singleNumber(self, N: List[int]) -> int:
        a = 0
        for n in N:
            a ^= n
        return a


"""
Runtime: 80 ms, faster than 95.71% of Python3 online submissions for Single Number.
Memory Usage: 15.3 MB, less than 8.20% of Python3 online submissions for Single Number.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
