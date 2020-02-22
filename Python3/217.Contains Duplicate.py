"""
@Title: 217. Contains Duplicate
@Tag: array / hashtable
@Date: Feb-22 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import collections


class Solution:
    def containsDuplicate(self, A: List[int]) -> bool:
        d = collections.defaultdict(int)
        for a in A:
            d[a] += 1
            if d[a] > 1:
                return True
        return False


"""
Runtime: 124 ms, faster than 84.43% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.1 MB, less than 16.98% of Python3 online submissions for Contains Duplicate.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
