"""
@Title: 1389. Create Target Array in the Given Order
@Tag: array
@Date: Mar-22 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, v in zip(index, nums):
            res.insert(i, v)
        return res


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
