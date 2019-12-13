"""
@Topic: 078. Subsets
@Tag: dfs/backtracking
@Date: Dec-13 2019
@Author: ceezyyy
@Difficulty: Medium 
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # the final res
        self.dfs(nums, [], 0, res)  # dfs + backtracking
        return res

    # index represent the current location of the element
    def dfs(self, nums: List[int], cur: List[int], index: int, res: List[List[int]]) -> None:
        res.append(cur[:])
        for i in range(index, len(nums)):
            cur.append(nums[i])
            self.dfs(nums, cur, i+1, res)
            cur.pop(-1)  # backtracking


"""
Runtime: 28 ms, faster than 95.64% of Python3 online submissions for Subsets.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Subsets.
"""
