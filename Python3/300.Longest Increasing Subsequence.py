"""
@Title: 300. Longest Increasing Subsequence
@Tag: dp
@Date: Dec-28 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # corner case
        if not nums:  # no subsequence
            return 0
        res = 1
        # record the length of the longest subsequence so far (subproblem)
        # initialization: set the default as one since each number is an increasing subsequence
        dp = [1]*len(nums)
        for k in range(len(nums)):  # the k-th element
            for i in range(k):  # scan pointer
                if nums[k] > nums[i]:  # increasing subsequence
                    dp[k] = max(dp[i]+1, dp[k])  # update the value
                    if dp[k] > res:
                        res = dp[k]  # update the res(the length of LIS)
        return res


"""
Runtime: 1276 ms, faster than 11.72% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.
"""


"""
Time complexity: O(n^2)
Space complexity: O(n)
"""


"""
Thanks to: @bephrem1 
Click: https://www.youtube.com/watch?v=fV-TF4OvZpk
"""
