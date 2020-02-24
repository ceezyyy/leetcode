"""
@Title: 209. Minimum Size Subarray Sum
@Tag: sliding window
@Date: Feb-24 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minSubArrayLen(self, s: int, A: List[int]) -> int:
        res, left, temp = float("inf"), 0, 0
        for i, a in enumerate(A):
            temp += a
            while temp >= s:
                res = min(res, i - left + 1)  # update the value first
                temp -= A[left]
                left += 1  # move the left boundary
        return res if res != float("inf") else 0


"""
Runtime: 72 ms, faster than 88.72% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 15.2 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
