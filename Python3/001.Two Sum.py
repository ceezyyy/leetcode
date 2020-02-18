"""
@Title: 001. Two Sum
@Tag: greedy
@Date: Feb-18 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Solution one:


class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] + a[j] == target:
                    return [i, j]


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


"""
Runtime: 5964 ms, faster than 10.64% of Python3 online submissions for Two Sum.
Memory Usage: 13.6 MB, less than 96.98% of Python3 online submissions for Two Sum.
"""


# Solution two:
