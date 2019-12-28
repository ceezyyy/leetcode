"""
@Title: 078. Subsets
@Tag: backtracking
@Date: Dec-28 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums, which is given a set of distinct numbers
        res = []  # the output
        subset = [None]*len(nums)  # initialization
        self.helper(nums, subset, 0, res)  # start from the index of zero
        return res

    # i stands for the index of current element whether we choose it or not
    def helper(self, nums: List[int], subset: List[int], i: int, res: List[List[int]]):
        if i == len(nums):  # already nailed it
            # get rid of the 'None' value, is similar to the 'set()'
            subset = [x for x in subset if x is not None]
            res.append(subset)  # append it to the res
        else:
            # not choose the current element (find it by the index 'i')
            subset[i] = None
            self.helper(nums, subset, i+1, res)  # recursion
            # choose
            subset[i] = nums[i]
            self.helper(nums, subset, i+1, res)  # recursion


"""
Runtime: 36 ms, faster than 62.06% of Python3 online submissions for Subsets.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Subsets.
"""
