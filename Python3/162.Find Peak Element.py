"""
@Title: 162. Find Peak Element
@Tag: array / binary search
@Date: Jan-22 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # nums[-1] = nums[n] = -∞
        nums.insert(0, float("-inf"))
        nums.insert(len(nums), float("-inf"))
        for i in range(1, len(nums) - 1):  # linear scan
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i - 1


"""
Runtime: 64 ms, faster than 7.76% of Python3 online submissions for Find Peak Element.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
