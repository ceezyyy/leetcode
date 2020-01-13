"""
@Title: 094. Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, node: TreeNode, res: List[int]) -> None:
        if not node:
            return
        if node.left:
            self.inorder(node.left, res)
        res.append(node.val)
        if node.right:
            self.inorder(node.right, res)


"""
Runtime: 20 ms, faster than 96.79% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
