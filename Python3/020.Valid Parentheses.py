"""
@Title: 020. Valid Parentheses
@Tag: stack / string
@Date: Jan-27 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        mapping, stack = {")": "(", "]": "[", "}": "{"}, []
        for ch in s:
            if ch in mapping.keys():  # right
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:  # left
                stack.append(ch)
        return not stack


"""
Runtime: 24 ms, faster than 90.29% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
