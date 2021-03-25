"""
@Title: 006. ZigZag Conversion
@Tag: string
@Date: Feb-21 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def convert(self, S: str, R: int) -> str:
        if R == 1 or R > len(S):  # corner case
            return S
        res, i, step = ['' for r in range(R)], 0, 0  # a string for each line
        for s in S:
            res[i] += s
            if i == 0:  # first row
                step = 1  # down
            if i == R - 1:  # last row
                step = -1  # up
            i += step
        return "".join(res)


"""
Runtime: 52 ms, faster than 86.77% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
"""
