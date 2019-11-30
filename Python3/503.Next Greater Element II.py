"""
@Topic: 503. Next Greater Element II
@Tag: stack
@Date: Nov-30 2019
@Author: ceezyyy
@Difficulty: Medium 
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # decreasing stack
        res = [-1]*len(nums)  # the initialization of output
        stack = []
        # [1 2 1] modified array is: [1 2 1 1 2 1] (actually does not exist)
        # start from 2*len(nums) since the array is circular
        for i in range(2*len(nums)-1, -1, -1):
            while stack and (nums[i % len(nums)] >= stack[-1]):
                stack.pop()
            if stack:
                res[i % len(nums)] = stack[-1]  # update the res
            stack.append(nums[i % len(nums)])
        return res


"""
Runtime: 280 ms, faster than 24.93% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Next Greater Element II.
"""
