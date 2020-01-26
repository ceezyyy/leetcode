"""
@Title: 1221. Split a String in Balanced Strings
@Tag: string
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, res = 0, 0
        for ch in s:
            if ch == "L":
                count += 1
            else:  # ch == "R"
                count -= 1
            if count == 0:
                res += 1
        return res


"""
Runtime: 28 ms, faster than 67.62% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
"""
