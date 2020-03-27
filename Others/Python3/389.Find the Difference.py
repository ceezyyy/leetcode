"""
@Title: 389. Find the Difference
@Tag: hashmap
@Date: Feb-23 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import collections as c


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = c.defaultdict(int)
        for ch in s:
            d[ch] += 1
        for ch in t:
            d[ch] -= 1
            if d[ch] < 0:
                return ch


"""
Runtime: 32 ms, faster than 69.08% of Python3 online submissions for Find the Difference.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Find the Difference.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
