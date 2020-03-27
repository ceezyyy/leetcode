"""
@Title: 1287. Element Appearing More Than 25% In Sorted Array
@Tag: array
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import collections


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common(1)[0][0]


"""
Runtime: 104 ms, faster than 21.14% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
"""
