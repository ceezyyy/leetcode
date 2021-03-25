"""
@Title: 053. Maximum Subarray
@Tag: dp
@Date: Dec-19 019
@Author: ceezyyy
@Difficulty: Easy
@Reference: @Back To Back SWE 
https://www.youtube.com/watch?v=2MmGzdiKR9Y
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # corner case
        if len(nums) == 1:  # containing at least one number
            return nums[0]
        dp = [0]*len(nums)  # memory
        dp[0] = nums[0]  # the first element / initialization
        res = dp[0]  # a crucial step, initialized the res to dp[0]
        for i in range(1, len(nums)):  # for loop
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i] > res:
                res = dp[i]  # update the res
        return res


"""
Runtime: 68 ms, faster than 82.83% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.5 MB, less than 90.24% of Python3 online submissions for Maximum Subarray.
"""
