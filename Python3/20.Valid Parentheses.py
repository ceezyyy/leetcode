"""
20. Valid Parentheses
Date: Oct-24 2019
Author: ceezyyy
Difficulty: Easy
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # type(stack)->list
        mapping = {')': '(', '}': '{', ']': '['}  # dict[closing]=opening
        for c in s:
            if c in mapping:  # closing bracket
                top_element = stack.pop() if stack else '#'
                if(mapping[c] != top_element):
                    return False
            else:
                stack.append(c)  # opening bracket
        return not stack


def test():
    s = Solution()
    print(s.isValid("(()[]{}"))


if __name__ == "__main__":
    test()
