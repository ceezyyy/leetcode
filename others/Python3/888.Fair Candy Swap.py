"""
@Title: 888. Fair Candy Swap
@Tag: array
@Date: Feb-02 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        for j in set(B):  # accelerate
            # solve the equation: "y - x = (sum(B) - sum(A)) / 2"
            if j - (sum(B) - sum(A)) // 2 in A:
                return [j - (sum(B) - sum(A)) // 2, j]


"""
Runtime: 6864 ms, faster than 5.16% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 15.1 MB, less than 41.67% of Python3 online submissions for Fair Candy Swap.
"""
