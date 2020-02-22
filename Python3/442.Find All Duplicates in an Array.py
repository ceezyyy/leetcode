"""
@Title: 442. Find All Duplicates in an Array
@Tag: array / hashtable
@Date: Feb-22 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import collections as c


class Solution:
    def findDuplicates(self, A: List[int]) -> List[int]:
        res, d = [], c.defaultdict(int)
        for a in A:
            d[a] += 1
            if d[a] == 2:
                res.append(a)
        return res


"""
Runtime: 392 ms, faster than 65.88% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.2 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
