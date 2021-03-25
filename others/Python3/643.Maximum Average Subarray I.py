"""
@Title: 643. Maximum Average Subarray I
@Tag: array
@Date: Jan-30 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, cur = 0, k - 1, 0  # initialization
        for i in range(k):  # first k elements
            cur += nums[i]
        res = cur
        while right + 1 < len(nums):
            left, right = left + 1, right + 1  # move on
            cur = cur - nums[left - 1] + nums[right]
            res = cur if cur > res else res
        return res / k


"""
Runtime: 1152 ms, faster than 6.92% of Python3 online submissions for Maximum Average Subarray I.
Memory Usage: 15.9 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
