"""
@Title: 682. Baseball Game
@Tag: Stack
@Date: Nov-16 2019
@Author: ceezyyy
@Difficulty: Easy
"""

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []  # score
        for op in ops:
            if op == '+':  # one round's score
                stack.append(stack[-1]+stack[-2])
            elif op == 'D':  # one round's score
                stack.append(2*stack[-1])
            elif op == 'C':  # an operation
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


def test():
    s = Solution()
    res = s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
    print(res)


if __name__ == "__main__":
    test()


"""
Runtime: 28 ms, faster than 99.89% of Python3 online submissions for Baseball Game.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Baseball Game.
"""
