"""
@Title: 144. Binary Tree Preorder Traversal
@Tag: binary tree
@Date: Jan-13 2020
@Author: ceezyyy
@Difficulty: Medium
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.pre(root, res)
        return res

    def pre(self, node: TreeNode, res: List[int]) -> None:
        if not node:
            return
        res.append(node.val)
        self.pre(node.left, res)
        self.pre(node.right, res)


"""
Runtime: 36 ms, faster than 8.29% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
