"""
@Title: 1337. The K Weakest Rows in a Matrix
@Tag: array
@Date: Feb-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Version one:


class Solution:
    def kWeakestRows(self, M: List[List[int]], k: int) -> List[int]:
        S = [[sum(m), i] for i, m in enumerate(M)]  # S -> [[soldiers, index]]
        S = sorted(S)  # weakest -> strongest
        # "s[1]" -> index, "[:k]" -> the first k rows
        return [s[1] for s in S][:k]


# Version two(1-line):


class Solution:
    def kWeakestRows(self, M: List[List[int]], k: int) -> List[int]:
        return [s[1] for s in sorted([[sum(m), i] for i, m in enumerate(M)])][:k]


"""
Runtime: 108 ms, faster than 92.47% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.
"""
