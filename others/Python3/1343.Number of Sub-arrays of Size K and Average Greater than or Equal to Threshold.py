"""
@Title: 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
@Tag: sliding window
@Date: Feb-10 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def numOfSubarrays(self, a: List[int], k: int, t: int) -> int:
        t, res, temp = t * k, 0, 0
        left = 1  # left pointer
        right = left + k - 1  # right pointer
        for i in range(k):  # the sum of first k element
            temp += a[i]
        if temp >= t:  # greater than or equal to
            res += 1
        while right < len(a):  # sliding window
            temp = temp - a[left - 1] + a[right]
            if temp >= t:  # greater than or equal to
                res += 1
            left, right = left + 1, right + 1
        return res


"""
Runtime: 700 ms, faster than 33.33% of Python3 online submissions for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold.
Memory Usage: 25.6 MB, less than 100.00% of Python3 online submissions for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
