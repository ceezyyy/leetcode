"""
@Title: 283. Move Zeroes
@Tag: array
@Date: Jan-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # corner case
        if len(nums) == 0 or len(nums) == 1:
            return
        index = 0  # record the number of the non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                # maintaining the relative order of the non-zero elements
                nums[index] = nums[i]
                index += 1  # count
        while index < len(nums):  # move all 0's to the end
            nums[index] = 0
            index += 1


"""
Runtime: 48 ms, faster than 86.96% of Python3 online submissions for Move Zeroes.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
