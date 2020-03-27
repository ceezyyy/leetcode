"""
@Title: 035. Search Insert Position
@Tag: binary search
@Date: Dec-21 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:  # corner case
            return 0
        left = 0  # left pointer
        right = len(nums)-1  # right pointer
        # binary search
        while(left < right):
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            # not equal
            if target < nums[mid]:  # target may on the left
                right = mid-1
            else:  # target may on the right
                left = mid+1
        # now, left == right
        if target == nums[left]:  # corner case
            return left
        else:
            if target < nums[left]:
                return left
            else:
                return left+1


"""
Runtime: 44 ms, faster than 96.95% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
"""
