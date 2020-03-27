"""
@Title: 013. Roman to Integer
@Tag: string
@Date: Jan-31 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol, res = {'I': 1, 'V': 5, 'X': 10,
                       'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0
        for i in range(len(s) - 1):
            if symbol[s[i]] < symbol[s[i+1]]:
                res -= symbol[s[i]]
            else:
                res += symbol[s[i]]
        res += symbol[s[-1]]  # always add the last element
        return res


"""
Runtime: 44 ms, faster than 73.05% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
