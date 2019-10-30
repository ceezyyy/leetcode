"""
@Title: 946. Validate Stack Sequences
@Tag: stack
@Date: Oct-26 2019
@Author: ceezyyy
@Difficulty: Medium
"""


import collections
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[0]:  # stack top
                stack.pop()
                popped.pop(0)
        return not stack


def test():
    s = Solution()
    print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))


if __name__ == "__main__":
    test()
