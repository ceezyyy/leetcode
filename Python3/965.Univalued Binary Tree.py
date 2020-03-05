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
        vals = []

        def dfs(root):
            if root:
                vals.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return len(set(vals)) == 1


"""
Runtime: 24 ms, faster than 92.45% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Univalued Binary Tree.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
