"""
@Title: 144. Binary Tree Preorder Traversal
@Tag: binary tree
@Date: Mar-01 2020
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()  # LIFO
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


"""
Runtime: 28 ms, faster than 64.97% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
