"""
@Title: 198. House Robber
@Tag: dp
@Date: Dec-20 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)  # memory
        # corner case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])
        # initialization
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0]+nums[2]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-3], dp[i-2])+nums[i]
        return max(dp[-1], dp[-2])


"""
Runtime: 28 ms, faster than 88.96% of Python3 online submissions for House Robber.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber.
"""
