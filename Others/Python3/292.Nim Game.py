"""
@Title: 292. Nim Game
@Tag: brainteaser
@Date: Jan-25 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


"""
Runtime: 40 ms, faster than 6.96% of Python3 online submissions for Nim Game.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Nim Game.
"""
