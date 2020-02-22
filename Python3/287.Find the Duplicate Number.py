"""
@Title: 287. Find the Duplicate Number
@Tag: array
@Date: Feb-22 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import collections


# Solution one(hashmap)


class Solution:
    def findDuplicate(self, A: List[int]) -> int:
        d = collections.defaultdict(int)
        for a in A:
            d[a] += 1
            if d[a] > 1:
                return a


"""
Runtime: 60 ms, faster than 94.71% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 15.1 MB, less than 17.86% of Python3 online submissions for Find the Duplicate Number.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
