"""
@Title: 965. Univalued Binary Tree
@Tag: binary tree
@Date: Mar-05 2020
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.dfs(root, root.val)

    def dfs(self, node, v):
        if node:
            return False if node.val != v else self.dfs(node.left, v) and self.dfs(node.right, v)
        return True


"""
Runtime: 24 ms, faster than 98.45% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Univalued Binary Tree.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
