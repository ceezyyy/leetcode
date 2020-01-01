"""
@Title: 189. Rotate Array
@Tag: array
@Date: Jan-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = nums.copy()  # a copy of nums, which means we create an extra space
        for i in range(len(nums)-1, -1, -1):  # reverse order
            nums[(i+k) % len(nums)] = new_nums[i]  # modify in-place


"""
Runtime: 64 ms, faster than 75.63% of Python3 online submissions for Rotate Array.
Memory Usage: 14.1 MB, less than 5.09% of Python3 online submissions for Rotate Array.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
