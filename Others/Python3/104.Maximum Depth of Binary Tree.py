"""
@Title: 104. Maximum Depth of Binary Tree
@Tag: binary tree
@Date: Mar-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)
        return max(left, right) + 1


"""
Runtime: 40 ms, faster than 68.10% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.5 MB, less than 93.75% of Python3 online submissions for Maximum Depth of Binary Tree.
"""


"""
"""
