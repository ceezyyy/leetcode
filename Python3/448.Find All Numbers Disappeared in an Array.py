"""
@Title: 448. Find All Numbers Disappeared in an Array
@Tag: array
@Date: Feb-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def findDisappearedNumbers(self, A: List[int]) -> List[int]:
        n, res = len(A), []
        A = set(A)
        for i in range(1, n+1):  # [1, n]
            if i not in A:
                res.append(i)
        return res


"""
Runtime: 356 ms, faster than 94.59% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22.9 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
