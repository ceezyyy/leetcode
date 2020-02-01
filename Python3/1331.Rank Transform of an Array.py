"""
@Title: 1331. Rank Transform of an Array
@Tag: array
@Date: Feb-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_rank = {}  # easy to add "key-value"
        for num in sorted(arr):
            if num not in num_rank:  # avoid duplicate element
                num_rank[num] = len(num_rank) + 1  # starting from 1
        return [num_rank[num] for num in arr]  # return List[int]


"""
Runtime: 384 ms, faster than 75.10% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 30.6 MB, less than 100.00% of Python3 online submissions for Rank Transform of an Array.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
