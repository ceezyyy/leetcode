"""
@Title: 268. Missing Number
@Tag: array
@Date: Jan-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)


"""
Runtime: 136 ms, faster than 91.51% of Python3 online submissions for Missing Number.
Memory Usage: 14 MB, less than 90.32% of Python3 online submissions for Missing Number.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
