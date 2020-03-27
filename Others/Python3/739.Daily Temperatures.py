"""
@Title: 739. Daily Temperatures
@Tag: stack
@Date: Nov-27 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # decreasing stack
        stack = []  # the index of T[i]
        res = [0]*len(T)  # initialized to 0
        for i in range(len(T)-1, -1, -1):
            # decreasing, notice that it should be '>='
            while stack and (T[i] >= T[stack[-1]]):
                stack.pop()
            if stack:
                res[i] = stack[-1]-i
            # if stack is empty, just append the index(of element) to the stack since the res[i] is initialized to 0
            stack.append(i)
        return res


"""
Runtime: 492 ms, faster than 94.54% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.6 MB, less than 73.68% of Python3 online submissions for Daily Temperatures.
"""

"""
References:

1. Monotonic Queue Explained with LeetCode Problems-Medium
https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6

2. LeetCode Monotone Stack Summary-Grandyang
https://www.cnblogs.com/grandyang/p/8887985.html

"""
