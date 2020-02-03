"""
@Title: 908. Smallest Range I
@Tag: math
@Date: Feb-03 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(A) - min(A) - 2 * K if max(A) - min(A) > 2 * K else 0


"""
Runtime: 116 ms, faster than 88.17% of Python3 online submissions for Smallest Range I.
Memory Usage: 13.8 MB, less than 88.89% of Python3 online submissions for Smallest Range I.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
