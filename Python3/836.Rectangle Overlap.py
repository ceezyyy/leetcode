"""
@Title: 836. Rectangle Overlap
@Tag: math
@Date: Jan-15 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width = min(rec1[2], rec2[2]) - max(rec1[0],
                                            rec2[0])  # min_right - max_left
        height = min(rec1[3], rec2[3]) - max(rec1[1],
                                             rec2[1])  # min_high - max_low
        return width > 0 and height > 0


"""
Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Rectangle Overlap.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rectangle Overlap.
"""
