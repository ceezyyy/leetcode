"""
@Title: 223. Rectangle Area
@Tag: math
@Date: Jan-15 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        width, height = min(C, G) - max(A, E), min(D, H) - max(B, F)
        overlap = height * width if (height > 0 and width > 0) else 0
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap


"""
Runtime: 44 ms, faster than 90.49% of Python3 online submissions for Rectangle Area.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rectangle Area.
"""
