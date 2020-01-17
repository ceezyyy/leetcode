"""
@Title: 844. Backspace String Compare
@Tag: stack
@Date: Jan-17 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for ch in S:
            if ch == "#":  # backspace
                if s:
                    s.pop()
            else:
                s.append(ch)
        for ch in T:
            if ch == "#":
                if t:
                    t.pop()
            else:
                t.append(ch)
        return s == t


"""
Runtime: 28 ms, faster than 70.38% of Python3 online submissions for Backspace String Compare.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
