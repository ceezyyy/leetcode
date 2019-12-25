"""
@Title: 055. Jump Game
@Tag: dp
@Date: Dec-25 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # corner case
        if len(nums) == 1:
            return True
        if nums[0] == 0 and len(nums) > 1:
            return False
        # memorization, furthest position (max index) that the current element can reach
        dp = [0]*len(nums)
        # initialization
        dp[0] = nums[0]  # dp[0]=nums[0]+0
        for i in range(1, len(nums)):  # bottom-up
            if dp[i-1] >= i:  # can reach the position of current element
                dp[i] = max(dp[i-1], nums[i]+i)  # furthest position so far
                if dp[i] >= len(nums)-1:  # can reach the final index
                    return True
            else:
                return False


"""
Runtime: 100 ms, faster than 59.33% of Python3 online submissions for Jump Game.
Memory Usage: 14.9 MB, less than 7.14% of Python3 online submissions for Jump Game.
"""
