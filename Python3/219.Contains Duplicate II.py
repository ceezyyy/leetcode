"""
@Title: 219. Contains Duplicate II
@Tag: hashset
@Date: Feb-23 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import collections as c


class Solution:
    def containsNearbyDuplicate(self, A: List[int], k: int) -> bool:
        d, flag = c.defaultdict(int), False  # hashset, flag
        for i, a in enumerate(A):  
            if a in d:  # appeared more than once
                if i - d[a] <= k:
                    flag = True
            d[a] = i  # value: position
        return flag


"""
Runtime: 96 ms, faster than 64.19% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 20.3 MB, less than 68.75% of Python3 online submissions for Contains Duplicate II.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
