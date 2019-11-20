"""
@Title: 150. Evaluate Reverse Polish Notation
@Tag: stack
@Date: Nov-20 2019
@Author: ceezyyy
@Difficulty: Medium
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # store the numbers, including the ans of each step, that shouble be taken into operation
        for op in tokens:
            if op == '+':
                # popped after calculating
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2+t1)  # push the ans into the stack
            elif op == '-':
                # popped after calculating
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2-t1)
            elif op == "*":
                # popped after calculating
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2*t1)
            elif op == '/':
                # popped after calculating
                t1 = stack.pop()
                t2 = stack.pop()
                # division between two integers should truncate toward zero.
                stack.append(int(t2/t1))
            else:
                stack.append(int(op))  # numbers
        return stack[0]  # after traversing, the last number is the answer


def test():
    s = Solution()
    res = s.evalRPN(["10", "6", "9", "3", "+", "-11",
                     "*", "/", "*", "17", "+", "5", "+"])  # 22
    print(res)


if __name__ == "__main__":
    test()


"""
Runtime: 64 ms, faster than 97.69% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
