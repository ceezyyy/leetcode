"""
@Title: 001. Two Sum
@Tag: hashmap
@Date: Feb-18 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Solution one(brute force):


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


# Solution two(hashmap):


class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        d = {}  # dict
        for i in range(len(a)):
            temp = target - a[i]
            if temp in d:
                return [i, d[temp]]
            d[a[i]] = i


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


"""
Runtime: 48 ms, faster than 79.17% of Python3 online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 62.09% of Python3 online submissions for Two Sum.
"""
