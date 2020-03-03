"""
@Title: 094. Binary Tree Inorder Traversal
@Tag: binary tree
@Date: Feb-03 2020
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the first element from the stack
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))  # as the "root"
                    stack.append((node.left, False))
        return res


"""
Runtime: 24 ms, faster than 87.53% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
