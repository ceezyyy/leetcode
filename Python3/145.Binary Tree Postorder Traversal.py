"""
@Title: 145. Binary Tree Postorder Traversal
@Tag: binary tree
@Date: Mar-03 2020
@Author: ceezyyy
@Difficulty: Hard
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res


"""
Runtime: 24 ms, faster than 87.85% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
