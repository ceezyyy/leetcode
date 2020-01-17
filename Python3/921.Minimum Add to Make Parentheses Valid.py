"""
@Title: 921. Minimum Add to Make Parentheses Valid
@Tag: stack
@Date: Jan-17 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res, stack = 0, []
        for ch in S:  # walk through
            if ch == "(":
                stack.append(ch)  # append it to stack
            else:  # ")"
                if stack:
                    stack.pop()  # match, and pop the "left" at the same time
                else:  # not match, since stack is empty, no more "left" to match the "right"
                    res += 1
        return res + len(stack)


"""
Runtime: 20 ms, faster than 98.24% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
