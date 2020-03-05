"""
@Title: 113. Path Sum II
@Tag: binary tree
@Date: Mar-05 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        res = []
        self.dfs(root, s, [], res)
        return res

    def dfs(self, node, s, temp, res):
        if node:
            temp.append(node.val)
            if not node.left and not node.right and s - node.val == 0:  # leaf and path_sum == 0
                res.append(temp)
                return
            self.dfs(node.left, s - node.val, temp.copy(), res)
            self.dfs(node.right, s - node.val, temp.copy(), res)


"""
Runtime: 40 ms, faster than 88.79% of Python3 online submissions for Path Sum II.
Memory Usage: 18 MB, less than 37.93% of Python3 online submissions for Path Sum II.
"""
