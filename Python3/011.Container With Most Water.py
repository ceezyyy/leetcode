"""
@Title: 011. Container With Most Water
@Tag: two pointers
@Date: Jan-25 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, res = 0, len(height) - 1, 0  # two pointers & max area
        while left < right:  # one pass
            res = max((right - left) * min(height[left], height[right]), res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


"""
Runtime: 152 ms, faster than 11.71% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.3 MB, less than 92.63% of Python3 online submissions for Container With Most Water.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
