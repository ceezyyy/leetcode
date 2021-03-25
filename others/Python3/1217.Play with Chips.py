"""
@Title: 1217. Play with Chips
@Tag: array
@Date: Feb-05 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def minCostToMoveChips(self, index: List[int]) -> int:
        odd, even = 0, 0
        for i in index:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)


"""
Runtime: 24 ms, faster than 95.04% of Python3 online submissions for Play with Chips.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Play with Chips.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
