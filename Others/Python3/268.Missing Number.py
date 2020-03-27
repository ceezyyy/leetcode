"""
@Title: 268. Missing Number
@Tag: array
@Date: Jan-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Approach 1: (Sum)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)


"""
Runtime: 136 ms, faster than 91.51% of Python3 online submissions for Missing Number.
Memory Usage: 14 MB, less than 90.32% of Python3 online submissions for Missing Number.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


# Approach 2: (Sort)


class Solution:
    def missingNumber(self, A: List[int]) -> int:
        A = sorted(A)
        if A[0] != 0:  # corner case
            return 0
        n = len(A)
        for i in range(1, n):
            if A[i] != A[i-1] + 1:
                return A[i] - 1
        return A[-1] + 1


"""
Runtime: 156 ms, faster than 24.68% of Python3 online submissions for Missing Number.
Memory Usage: 14 MB, less than 83.87% of Python3 online submissions for Missing Number.
"""


"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
