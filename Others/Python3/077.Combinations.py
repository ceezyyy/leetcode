"""
@Topic: 077. Combinations
@Tag: dfs/backtracking
@Date: Dec-13 2019
@Author: ceezyyy
@Difficulty: Medium 
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n >= k:  # avoid corner case
            self.dfs(n, k, 1, [], res)  # dfs/backtracking
        return res

    def dfs(self, n: int, k: int, index: int, cur: List[int], res: List[int]):
        if len(cur) == k:  # the exit of dfs
            res.append(cur[:])  # deep copy
        for i in range(index, n+1):
            cur.append(i)
            self.dfs(n, k, i+1, cur, res)
            cur.pop()  # backtracking


"""
Runtime: 552 ms, faster than 57.89% of Python3 online submissions for Combinations.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Combinations.
"""
