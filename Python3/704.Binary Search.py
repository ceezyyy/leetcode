"""
@Title: 704. Binary Search 
@Tag: binary search
@Date: Dec-27 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1  # left & right bound
        while left <= right:
            mid = (left+right)//2  # the half
            if target == nums[mid]:  # nailed it
                return mid  # return the index
            else:  # not found
                if target > nums[mid]:  # the right part
                    left = mid+1
                else:  # the left part
                    right = mid-1
        # If target exists then return its index, otherwise return -1
        return -1


"""
Runtime: 248 ms, faster than 99.30% of Python3 online submissions for Binary Search.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Binary Search.
"""
