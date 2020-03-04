"""
@Title: 169. Majority Element
@Tag: hashtable
@Date: Mar-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import collections as c


class Solution:
    def majorityElement(self, A: List[int]) -> int:
        d = c.defaultdict(int)
        for a in A:
            d[a] += 1
            if d[a] > len(A) // 2:
                return a


"""
Runtime: 192 ms, faster than 28.49% of Python3 online submissions for Majority Element.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Majority Element.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
