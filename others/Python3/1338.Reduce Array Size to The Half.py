"""
@Title: 1338. Reduce Array Size to The Half
@Tag: array
@Date: Feb-11 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import collections


class Solution:
    def minSetSize(self, A: List[int]) -> int:
        res, temp, n = 0, 0, len(A) / 2
        for a, freq in collections.Counter(A).most_common():
            temp += freq  # the number of the elements which should be removed
            res += 1
            if temp >= n:  # at least half of the integers of the array are removed
                return res
        return res


"""
Runtime: 616 ms, faster than 85.79% of Python3 online submissions for Reduce Array Size to The Half.
Memory Usage: 34.3 MB, less than 100.00% of Python3 online submissions for Reduce Array Size to The Half.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
